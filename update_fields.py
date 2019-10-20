import os

import sys
from tkinter import messagebox

import datetime
from PIL import ImageTk

__author__ = 'Mark Baker  email: mark2182@mac.com'


def resource_path(relative):
    """Utility function for Pyinstaller (which can generate a single file
    Windows executable). Enables correct file paths to be determined
    regardless of the the app being run in development mode or from the
    executable file. Pyinstaller generates the _MEIPASS directory"""

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def format_datetime(isotime):
    """Format iso time e.g. 2017-08-09T12:41:00Z into 091241Z format
    commonly used in Meteorology """
    # if isotime is not '':
    #     dtg = datetime.datetime.strptime(isotime, "%Y-%m-%dT%H:%M:%SZ")
    #     display_dtg = dtg.strftime("%d%H%MZ")
    #
    # else:
    #     display_dtg = ''

    return isotime


class UpdateFields:
    """Update the main window display fields with latest data"""
    def __init__(self):

        # Load the images (colour state boxes etc.) used in the application
        # Example of file path that doesn't use the 'resource_path' function
        # but wont work with Pyinstaller: self.tick =
        # ImageTk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
        # 'images/tick.gif'))

        self.tick = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'tick.gif')))
        self.cross = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'cross.gif')))
        self.notaf = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'notaf.gif')))
        self.blue = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'blue.gif')))
        self.white = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'white.gif')))
        self.green = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'green.gif')))
        self.yellow1 = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'yellow1.gif')))
        self.yellow2 = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'yellow2.gif')))
        self.amber = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'amber.gif')))
        self.red = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'red.gif')))
        self.grey = ImageTk.PhotoImage(file=resource_path(os.path.join(
            'images', 'grey.gif')))

        self.alert_string = ''
        self.status_change = False

    def update_icao0(self, icao_dict, main_view):
        """For each ICAO we set the appropriate text and colour state boxes
        etc. with data from the stations dictionary"""
        main_view.app_view.icao0.set(icao_dict['ICAO'])
        main_view.app_view.icao0_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao0_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao0_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao0_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao1(self, icao_dict, main_view):

        main_view.app_view.icao1.set(icao_dict['ICAO'])
        main_view.app_view.icao1_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao1_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao1_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao1_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao2(self, icao_dict, main_view):

        main_view.app_view.icao2.set(icao_dict['ICAO'])
        main_view.app_view.icao2_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao2_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict[
                                                  'PREV_COLOUR'])))
        main_view.app_view.icao2_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict[
                                                  'LATEST_COLOUR'])))
        main_view.app_view.icao2_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao3(self, icao_dict, main_view):

        main_view.app_view.icao3.set(icao_dict['ICAO'])
        main_view.app_view.icao3_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao3_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao3_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao3_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao4(self, icao_dict, main_view):

        main_view.app_view.icao4.set(icao_dict['ICAO'])
        main_view.app_view.icao4_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao4_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao4_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao4_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao5(self, icao_dict, main_view):

        main_view.app_view.icao5.set(icao_dict['ICAO'])
        main_view.app_view.icao5_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao5_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao5_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao5_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao6(self, icao_dict, main_view):

        main_view.app_view.icao6.set(icao_dict['ICAO'])
        main_view.app_view.icao6_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao6_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao6_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao6_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao7(self, icao_dict, main_view):

        main_view.app_view.icao7.set(icao_dict['ICAO'])
        main_view.app_view.icao7_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao7_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao7_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao7_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao8(self, icao_dict, main_view):

        main_view.app_view.icao8.set(icao_dict['ICAO'])
        main_view.app_view.icao8_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao8_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao8_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao8_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def update_icao9(self, icao_dict, main_view):

        main_view.app_view.icao9.set(icao_dict['ICAO'])
        main_view.app_view.icao9_time.set(format_datetime(icao_dict[
                                                              'METAR_TIME']))
        main_view.app_view.icao9_prev_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['PREV_COLOUR'])))
        main_view.app_view.icao9_latest_colour_field.configure(
            image=(self.get_colourstate_label(icao_dict['LATEST_COLOUR'])))
        main_view.app_view.icao9_taf_status_field.configure(
            image=(self.get_tafstatus_label(icao_dict['TAF_STATUS'])))

    def display_alerts(self, icao_dict, view):
        """Determine if a colour state change has occurred and display alert
        dialog if necessary. Don't alert if previous or latest colour states
        are grey (0). Only alert if a the colourstate change is as the result
        of a new METAR message
        :param view: """
        if icao_dict['PREV_COLOUR'] is not 0 and icao_dict['LATEST_COLOUR'] \
                is not 0:
            if icao_dict['LATEST_COLOUR'] < icao_dict['PREV_COLOUR'] and\
                    icao_dict['NEW_METAR'] == True:
                # alert = AlertDialog(controller.root)
                # alert.deterioration_alert(icao_dict['ICAO'] +
                # ' Deteriorated')
                self.alert_string += icao_dict['ICAO'] + \
                                     ' Deteriorated - ' + \
                                     self.get_coloursate_text(
                                         icao_dict['LATEST_COLOUR']) + '\r'
                self.status_change = True

            elif icao_dict['LATEST_COLOUR'] > icao_dict['PREV_COLOUR'] and \
                    icao_dict['NEW_METAR'] == True:
                # alert = AlertDialog(controller.root)
                # alert.improvement_alert(icao_dict['ICAO'] + ' Improvement')
                self.alert_string += \
                    icao_dict['ICAO'] + ' Improvement - ' + \
                    self.get_coloursate_text(icao_dict['LATEST_COLOUR']) + '\r'
                self.status_change = True

        if icao_dict['TAF_STATUS'] is 1 and icao_dict['NEW_METAR']:
            self.alert_string += icao_dict['ICAO'] + ' TAF bust!\r'
            self.status_change = True

    def trigger_alert(self):
        messagebox.showinfo('Status Change', self.alert_string)
        self.status_change = False
        self.alert_string = ''

    @staticmethod
    def set_icao_fields(main_view, icao_list):
        """set the ICAO fields to the last set if available"""
        if icao_list:
            main_view.app_view.icao0.set(icao_list[0])
            main_view.app_view.icao1.set(icao_list[1])
            main_view.app_view.icao2.set(icao_list[2])
            main_view.app_view.icao3.set(icao_list[3])
            main_view.app_view.icao4.set(icao_list[4])
            main_view.app_view.icao5.set(icao_list[5])
            main_view.app_view.icao6.set(icao_list[6])
            main_view.app_view.icao7.set(icao_list[7])
            main_view.app_view.icao8.set(icao_list[8])
            main_view.app_view.icao9.set(icao_list[9])

    def set_colourstates_grey(self, main_view):
        """Set all the colourstate fields to grey (used at app startup)"""
        main_view.app_view.icao0_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao0_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao0_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao1_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao1_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao1_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao2_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao2_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao2_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao3_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao3_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao3_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao4_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao4_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao4_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao5_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao5_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao5_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao6_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao6_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao6_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao7_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao7_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao7_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao8_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao8_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao8_taf_status_field.configure(
            image=self.notaf)
        main_view.app_view.icao9_prev_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao9_latest_colour_field.configure(
            image=self.grey)
        main_view.app_view.icao9_taf_status_field.configure(
            image=self.notaf)

    def get_colourstate_label(self, colourstate):
        """Determine which colour image box to assign based on
        the colourstate"""
        colourstate_label = None

        if colourstate == 0:
            colourstate_label = self.grey
        elif colourstate == 1:
            colourstate_label = self.red
        elif colourstate == 2:
            colourstate_label = self.amber
        elif colourstate == 3:
            colourstate_label = self.yellow2
        elif colourstate == 4:
            colourstate_label = self.yellow1
        elif colourstate == 5:
            colourstate_label = self.green
        elif colourstate == 6:
            colourstate_label = self.white
        elif colourstate == 7:
            colourstate_label = self.blue

        return colourstate_label

    @staticmethod
    def get_coloursate_text(colourstate):
        """Determine which colourstate text to use for a given
        colourstate number"""
        colourstate_text = ''

        if colourstate == 0:
            colourstate_text = ''
        elif colourstate == 1:
            colourstate_text = 'RED'
        elif colourstate == 2:
            colourstate_text = 'AMB'
        elif colourstate == 3:
            colourstate_text = 'YL02'
        elif colourstate == 4:
            colourstate_text = 'YL01'
        elif colourstate == 5:
            colourstate_text = 'GRN'
        elif colourstate == 6:
            colourstate_text = 'WHT'
        elif colourstate == 7:
            colourstate_text = 'BLU'

        return colourstate_text

    def get_tafstatus_label(self, tafstatus):
        """Determine which graphic image to use for a given
        TAF status number"""
        tafstatus_label = None

        if tafstatus == 0:
            # TAF OK
            tafstatus_label = self.tick
        elif tafstatus == 1:
            # TAF bust
            tafstatus_label = self.cross
        elif tafstatus == 2:
            # No TAF
            tafstatus_label = self.notaf

        return tafstatus_label
