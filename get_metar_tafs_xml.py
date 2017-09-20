import sys

import os
from lxml import etree
import socket
import requests
import pickle

if sys.version_info[0] < 3:
    import tkMessageBox
else:
    from tkinter import messagebox as tkMessageBox

__author__ = 'Mark Baker  email: mark2182@mac.com'


def update_report_data(icao0, icao1, icao2, icao3, icao4, icao5, icao6, icao7, icao8, icao9):
    """Get the latest METAR and TAF report data for the input ICAO code, this is in the format of an XML tree that can
    be parsed to get the required data. The Web Feature Service (WFS) is provided by FSD's Visual Weather 4.0.3 sandbox
    server. Note that this server resides within the DMZ and is not available through DirectAccess connections.
    exvinnsandbxvw02 is the operational server and exvinnsandbxvw01 the test server"""

    global root
    socket.setdefaulttimeout(5)

    icao_string = icao0+','+icao1+','+icao2+','+icao3+','+icao4+','+icao5+','+icao6+','+icao7+','+icao8+','+icao9
    icao_list = [icao0, icao1, icao2, icao3, icao4, icao5, icao6, icao7, icao8, icao9]

    save_icao_list(icao_list) # Save the currently entered ICAO's between sessions.

    # Query WFS server to get the latest METAR/TAF XML data
    try:
        root = etree.fromstring(requests.get
                                ('http://exvinnsandbxvw02:8008/OBSERVATIONS?SERVICE=WFS&VERSION=1.0.0&REQUEST'
                                 '=GetFeature&TYPENAME=LatestMETAR,LatestTAF&ICAO='+icao_string,
                                 timeout=9, headers={'Connection': 'close'}).content)

        """Following lines allow for testing using an XML file located in the current working directory"""
        # parser = etree.XMLParser()
        # tree = etree.parse('OBSERVATIONS.xml', parser)
        # root = tree.getroot()

    except requests.exceptions.RequestException as e:
        pass
        tkMessageBox.showerror('Communications Error', 'Error retrieving data - will retry...')

    return root


def get_latest_metar(icao):
    """Returns a string list with the issue time and latest METAR report for the given ICAO argument"""
    namespace = '{http://www.iblsoft.com/wfs}'
    issue_time = ''
    metar = ''

    """Iterate through the XML root to find LatestMETAR instances"""
    for element in root.iter(namespace + 'LatestMETAR'):
        """Locate ICAO element """
        for icao_text in element.iter(namespace + 'ICAO'):
            """Check if ICAO element matches icao argument"""
            if icao_text.text.capitalize() == icao.capitalize():
                """If icao matches extract the METAR from the reportText element"""
                for report_text in element.iter(namespace + 'reportText'):

                    metar = report_text.text
                    """Extract the issue time of the report from the issueTime element"""
                    for issue_time in element.iter(namespace + 'issueTime'):
                        issue_time = issue_time.text

    return issue_time, metar


def get_latest_taf(icao):
    """Returns a string list with the issue time and latest TAF report for the given ICAO argument"""
    namespace = '{http://www.iblsoft.com/wfs}'
    issue_time = ''
    taf = ''

    """Iterate through the XML root to find LatestTAF instances"""
    for element in root.iter(namespace + 'LatestTAF'):
        """Locate ICAO element """
        for icao_text in element.iter(namespace + 'ICAO'):
            """Check if ICAO element matches icao argument"""
            if icao_text.text.capitalize() == icao.capitalize():
                """If icao matches extract the METAR from the reportText element"""
                for report_text in element.iter(namespace + 'reportText'):

                    taf = report_text.text
                    """Extract the issue time of the report from the issueTime element"""
                    for issue_time in element.iter(namespace + 'issueTime'):
                        issue_time = issue_time.text

    return issue_time, taf


def save_icao_list(icao_list):
    """Saves the present ICAO's to a file"""
    try:
        if os.path.exists('.icao_list.conf'):
            os.system('attrib -h .icao_list.conf')
        with open('.icao_list.conf', 'wb') as icaos:
            pickle.dump(icao_list, icaos)
            os.system('attrib +h .icao_list.conf')

    except IOError as err:
        print('ICAO list save file error: ' + str (err))
    except pickle.PickleError as perr:
        print('ICAO list save pickling error: ' + str(perr))


# Test this module
if __name__ == "__main__":
    """Get latest METAR/TAF report data from 10 ICAO's"""
    update_report_data('EGUW', 'EGSS', 'EGLL', 'EGBB', 'EGDM', 'EGDY', 'EGEC', 'EGGD', 'EGGP', 'EGHE')
    """Print out issue time and latest METAR and TAF for specified ICAO (ICAO's must be included in update report
    data call above"""
    print(get_latest_metar('EGUW'))
    print(get_latest_taf('EGUW'))

