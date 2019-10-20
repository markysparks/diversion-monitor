import datetime
import re
import socket
import requests
from tkinter import messagebox as tkMessageBox

__author__ = 'Mark Baker  email: mark.baker@metoffice.gov.uk'

icao_metars = []
icao_tafs = []
regex_issue_time = re.compile('\d\d\d\d\d\dZ')


def update_report_data(icao0='', icao1='', icao2='', icao3='', icao4='', icao5='', icao6='', icao7='', icao8='', icao9=''):
    socket.setdefaulttimeout(8)
    response_metars = ''
    response_tafs = ''

    icao_list = [icao0, icao1, icao2, icao3, icao4, icao5, icao6, icao7, icao8, icao9]

    """Get the latest METAR for specified ICAOs, format: &stn01=EGUW&stn02=EGLL&stn03=EGSS"""
    station_str = '&stn01=' + icao0 + '&stn02=' + icao1 + '&stn03=' + icao2 + '&stn04=' + icao3 + '&stn05=' + icao4 + \
                  '&stn06=' + icao5 + '&stn07=' + icao6 + '&stn08=' + icao7 + '&stn09=' + icao8 + '&stn10=' + icao9

    db_rqst_str_metars = 'http://mdbdb-prod/cgi-bin/moods/webret.pl?pageType=mainpage&subtype=METARS&system=mdbdb' \
                         '-prod&idType=ICAO' + station_str + '&submit=Retrieve+Latest+Report'

    db_rqst_str_tafs = 'http://mdbdb-prod/cgi-bin/moods/webret.pl?pageType=mainpage&subtype=TAFS&system=mdbdb' \
                       '-prod&idType=ICAO' + station_str + '&submit=Retrieve+Latest+Report'

    # example response = 'Obs returned = 0003 CODE NAME -: mdb VERSION ---: 4.25.0 COMPILED @ : 10:32:54 on Jul 19 2016
    # LATEST PLATFORM EGLL EGSS EGUW ELEMENTS MTR_RPT_TXT RCT_DAY RCT_HR RCT_MNT ICAO_ID DAY HR MNTRTABLE: Retrieval
    # table
    # used: /usr/local/moods/tables//retrieval_tableRTABLE: TABLES base location: /usr/local/moods/tables/ddhhmmZ
    # ident report 270850Z EGLL  EGLL 270850Z 23012KT 9999 SCT012 BKN018 18/17 Q1015 TEMPO BKN014 270850Z EGSS  EGSS
    # 270850Z AUTO 23010KT 9999 -RA BKN005 17/16 Q1014 REDZ 270850Z EGUW  EGUW 270850Z AUTO 24010KT 4500 RA BKN009
    # OVC014 17/16 Q1014 GRN BECMG 7 000 -RA GRN'

    # Query to get the latest METAR web page result
    try:
        response_metars = requests.get(db_rqst_str_metars)
        response_tafs = requests.get(db_rqst_str_tafs)
    except requests.exceptions.RequestException as e:
        pass
        tkMessageBox.showerror('Communications Error',
                               'Error retrieving data from MetDB - will retry if monitoring on.')

    # Check we have a response to our query before proceeding then for each ICAO specified
    # search the response for a matching METAR.
    if response_metars is not None:
        for icao in icao_list:
            metar = re.search(icao + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+?\\n\\n', response_metars.text)
            if metar:
                icao_metars.append(metar.group())

        # Different search expression required for last METAR in list list due to MetDB web page
        # response formatting.
        metar_last = re.search(icao9 + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+?\\n\s</pre>', response_metars.text)
        if metar_last:
            icao_metars.append(metar_last.group())

    # Check we have a response to our query before proceeding then for each ICAO specified
    # search the response for a matching METAR.
    if response_tafs is not None:
        for icao in icao_list:
            taf = re.search(icao + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+?\\n\\n', response_tafs.text)
            if taf:
                icao_tafs.append(taf.group())

        # Different search expression required for last METAR in list list due to MetDB web page
        # response formatting.
        taf_last = re.search(icao9 + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+?\\n\s</pre>', response_tafs.text)
        if taf_last:
            icao_tafs.append(taf_last.group())


def get_latest_metar(icao):
    # Expression to find the required METAR using the ICAO code
    regex_metar = re.compile(icao + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+')
    # Find the required METAR from the list of METARs
    metar_list = ([m.group(0) for l in icao_metars for m in [regex_metar.search(l)] if m])
    if len(metar_list) > 0:
        # Strip out occurrences of 15 multiple spaces that occur when web page response line wraps
        metar = re.sub('               ', '', metar_list[0]).strip()
        # Strip out any newlines and other cruft from web page response formatting
        metar = re.sub('\\n', '', metar).strip()
        metar = re.sub('\s</pre>', '', metar).strip()

        # Find the METAR issue time
        issue_time = ([m.group(0) for l in metar_list for m in [regex_issue_time.search(l)] if m])[0]

        return issue_time, metar
    else:
        return '', ''


def get_latest_taf(icao):
    # Expression to find the required TAF using the ICAO code
    regex_taf = re.compile(icao + '\s\d\d\d\d\d\dZ[\s\S\d\D\w\W]+')
    # Find the required TAF from the list of TAFs
    taf_list = ([m.group(0) for l in icao_tafs for m in [regex_taf.search(l)] if m])
    if len(taf_list) > 0:
        # Strip out occurrences of 15 multiple spaces that occur when web page response line wraps
        taf = re.sub('               ', '', taf_list[0]).strip()
        # Strip out any newlines and other cruft from web page response formatting
        taf = re.sub('\\n', '', taf).strip()
        taf = re.sub('\s</pre>', '', taf).strip()

        # Find the TAF issue time
        issue_time = ([m.group(0) for l in taf_list for m in [regex_issue_time.search(l)] if m])[0]

        return issue_time, taf
    else:
        return '', ''


if __name__ == "__main__":
    # print('METAR Data= ', get_metar_data('EGSS', 'EGLL', 'EGKK', 'EGUW', 'EGXE', 'EGTE', 'EGWU', 'EGUB'))
    update_report_data('EGSS', 'EGLL', 'EGUW')
    print(icao_metars)
    print(get_latest_metar('EGLL'))
    print(icao_tafs)
    print(get_latest_taf('EGUW'))
