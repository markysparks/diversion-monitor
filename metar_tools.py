import re
from fractions import Fraction

__author__ = 'Mark Baker  email: mark.baker@metoffice.gov.uk'


def metar_no_trend(metar):
    """Remove text after Q group - this removes any trend text (UK METAR's) which could interfere with
    current cloud state/visibility determination."""
    metar_notrend = metar.rsplit('Q', 1)[0]
    return metar_notrend


def get_vis_fm_mtrs(message):
    """Extract the minimum visibility value from a METAR or TAF report"""
    # Remove any trend message appended to a METAR
    message_txt = metar_no_trend(message)

    # Visibility is reported in metres using 4 digits e.g. 0250, 2000 , 7000 with 9999 meaning 10 KM or more
    search_string_metres = '\s\d\d\d\d\s'
    # US stations report visibility in statute miles e.g. 1/2SM, 1 3/4SM 5SM P6SM (more than 6 statute miles) in TAFs
    search_string_sm = """
             (?<= \s )
             (?P<more> P){0,1} # "P" prefix indicates visibility more than
             (?P<range> \d | \d/\d | \d\s\d/\d)    # More than 6 is always just P6SM
             (?P<unit> SM)                # Statute miles
             (?= \s|$ )
         """
    # Find any occurrences of visibilities in metres
    vis_list_metres = re.findall(search_string_metres, message_txt)

    # Check for CAVOK in massage - implies vis 10 KM or more
    if re.search('CAVOK', message_txt):
        vis_list_metres.append('9999')

    vis_list_sm = re.findall(search_string_sm, message_txt, re.VERBOSE)

    # Catch any statue miles visibility 10 SM (found in METARS) or above (not captured by search_string_sm above)
    if re.search('\s\d\dSM', message_txt):
        vis_list_sm.append(('P', '10', 'SM'))

    # If list is not empty, convert all the string elements in the list to integers before returning the minimum value
    if vis_list_metres:
        vis_list_metres = list(map(int, vis_list_metres))
        return int(min(vis_list_metres))

    # If no visibilities in metres check for visibility in statute miles (SM) - US stations
    elif vis_list_sm:

        list_sm_decimal = []
        list_metres = []
        if vis_list_sm:
            for vis in vis_list_sm:
                list_sm_decimal.append(float(sum(Fraction(s) for s in vis[1].split())))
                for vis2 in list_sm_decimal:
                    list_metres.append(int(vis2 * 1613))

        return int(min(list_metres))

    # No visibilities detected return -1 to ensure colour state will be zero (grey box)
    else:
        return -1


def get_sig_cloud_height(message):
    """Extract minimum significant cloud height base (SCT/BKN/OVC) fromm METAR or TAF report"""
    # Remove any trend message appended to a METAR
    message_txt = metar_no_trend(message)

    cloud_base_list_sct = re.findall('SCT\d\d\d', message_txt)
    cloud_base_list_bkn = re.findall('BKN\d\d\d', message_txt)
    cloud_base_list_ovc = re.findall('OVC\d\d\d', message_txt)
    cloud_base_list_vv = re.findall('VV\d\d\d', message_txt)

    if re.search('VV', message_txt):
        if re.search('VV///', message_txt):
            cloud_base_list_vv.append('0')

    cloud_base_list = cloud_base_list_sct + cloud_base_list_bkn + cloud_base_list_ovc + cloud_base_list_vv

    # Extract the digits from cloud groups
    cloud_base_list = [extract_digits(text) for text in cloud_base_list]
    # Cast all the cloud base elements to integers
    cloud_base_list = list(map(int, cloud_base_list))
    # Multiply each element by 100 to get the tru cloud height e.g. 010 = 1000  030 = 3000
    cloud_base_list = [value * 100 for value in cloud_base_list]

    if cloud_base_list:
        return int(min(cloud_base_list))
    else:
        # Ensure 2500ft (BLU) in case only 'FEW' amounts in report
        return 2500


def get_colourstate_nbr(report_txt):
    """Returns the colour state for a given cloud base (in ft) and visibility (in metres). A single digit is also
    returned to assist in past/present colour state comparisons where 7=BLU, 6=WHT, 5=GRN, 4=YLO1, 3=YLO2,
    2=AMB, 1=RED, 0= no colour state (grey)"""
    colourstate_nbr = 0

    visibility = get_vis_fm_mtrs(report_txt)
    cloudbase = get_sig_cloud_height(report_txt)
    # print('vis: ' + str(visibility))
    # print('cloud: ' + str(cloudbase))

    if visibility == -1 or cloudbase == -1:
        colourstate_nbr = 0  # GREY - unable to determine colourstate
    elif visibility < 800 or cloudbase < 200:
        colourstate_nbr = 1  # RED
    elif visibility < 1600 or cloudbase < 300:
        colourstate_nbr = 2  # AMB
    elif visibility < 2500 or cloudbase < 500:
        colourstate_nbr = 3  # YLO2
    elif visibility < 3700 or cloudbase < 700:
        colourstate_nbr = 4  # YLO1
    elif visibility < 5000 or cloudbase < 1500:
        colourstate_nbr = 5  # GRN
    elif visibility < 8000 or cloudbase < 2500:
        colourstate_nbr = 6  # WHT
    elif visibility > 7999 and cloudbase > 2499:
        colourstate_nbr = 7  # BLU
    else:
        colourstate_nbr = 0  # GREY - unable to determine colourstate

    return colourstate_nbr


def extract_digits(text):
    """Utility to extract digits from string using regex"""
    digits = re.search(r'\d+', text).group()

    return digits


def get_report_time(metar):
    """Utility to extract the report time from the message (in the format e.g. 190350Z  dayHourMinuteZ"""
    search_string = '\d\d\d\d\d\dZ'
    report_dtg = re.search(search_string, metar).group()
    return report_dtg


def extract_metar(icao, metdb_response_text):  # Not used at present
    metar = ''
    # print('doing  extract metar....')
    """extract metar message from metdb response text response. Add 000000Z time group on end of data block
        to assist with regex searching"""
    # msgstr = str(metdb_response_text.text)
    # print('MetDB response:')
    # print(metdb_response_text.text)
    searchstr1 = icao + r'\s\d\d\d\d\d\dZ[\s\S]*?\d\d\d\d\d\dZ'
    # searchstr1 = icao + r'\s\d\d\d\d\d\dZ.*?\n*?\r*?.*?\n*?\r*?.*?\n*?\r*?.*?\s\d\d\d\d\d\dZ'
    # searchstr2 = icao + r'\s\d\d\d\d\d\dZ.*?\n*?\r*?.*?\n*?\r*?.*?\n*?\r*?.*?\s<'
    searchstr2 = icao + r'\s\d\d\d\d\d\dZ[\s\S]</pre>'

    if re.search(searchstr1, metdb_response_text.text):
        metar_raw = re.search(searchstr1, metdb_response_text.text)
        metar = (metar_raw.group())[:-7]
        # print('METAR search1')
        # print(metar)

    elif re.search(searchstr2, metdb_response_text.text):
        metar_raw = re.search(searchstr2, metdb_response_text.text)
        metar = (metar_raw.group())[:-5]
        # print('METAR search2')
        # print(metar)

    else:
        print('METAR search failed')
    return metar


def test_suite(report_txt):
    vis = get_vis_fm_mtrs(report_txt)
    print('lowest vis =  ' + str(vis))

    low_cloud = get_sig_cloud_height(report_txt)
    print('lowest cloud = ' + str(low_cloud))

    colour_state = get_colourstate_nbr(report_txt)
    print('colour state = ' + str(colour_state))


if __name__ == "__main__":
    report = 'EGWU 091035Z 0912/1006 34007KT 9999 -RA BKN010 TEMPO 0912/0920 5000 RA PROB40 TEMPO 0912/0920 3000 ' \
              '+RA PROB30 TEMPO 0915/0919 36015G25KT FEW010 BKN015 BECMG 0919/0921 BKN018 BECMG 0921/0924 SCT030 ' \
              'PROB30 1000/1006 SCT010='

    test_suite(report)
