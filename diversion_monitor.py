#!/usr/bin/env python
__author__ = 'Mark Baker  email: mark2182@mac.com'
import datetime
import logging
import os
import pickle
import sys

import get_metar_tafs_xml as get_xml_data
import monitor_gui as gui

from metar_taf_dialog import MetarTafDialog
from station_data import StationData
from update_fields import UpdateFields
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

logging.basicConfig()

if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk


class Controller:
    """Main GUI controller, handles mouse, keyboard and data change events."""

    def __init__(self):
        self.root = tk.Tk()
        self.main_view = gui.MainView(self.root)

        self.latest_time = None

        self.monitoring = False
        self.update_fields = UpdateFields()

        """Dictionaries for holding ICAO station message and colour 
        state parameters etc."""
        self.icao0_data = StationData()
        self.icao1_data = StationData()
        self.icao2_data = StationData()
        self.icao3_data = StationData()
        self.icao4_data = StationData()
        self.icao5_data = StationData()
        self.icao6_data = StationData()
        self.icao7_data = StationData()
        self.icao8_data = StationData()
        self.icao9_data = StationData()

        self.main_view.controls_view.monitor_button.bind('<Button>',
                                                         self.start_monitor)
        self.main_view.controls_view.monitor_button.bind('<Return>',
                                                         self.start_monitor)

        self.main_view.controls_view.exit_button.bind('<Button>',
                                                      self.exit_app)
        self.main_view.controls_view.exit_button.bind('<Return>',
                                                      self.exit_app)

        self.main_view.controls_view.update_data_button.bind(
            '<Button>', self.update_data_now)
        self.main_view.controls_view.update_data_button.bind(
            '<Return>', self.update_data_now)

        self.main_view.app_view.icao0_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao1_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao2_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao3_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao4_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao5_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao6_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao7_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao8_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao9_entry.bind('<KeyRelease>', self.caps)

        self.main_view.app_view.viewICAO0_button.bind(
            '<Button>', self.view_metar_taf_icao0_data)
        self.main_view.app_view.viewICAO0_button.bind(
            '<Return>', self.view_metar_taf_icao0_data)
        self.main_view.app_view.viewICAO1_button.bind(
            '<Button>', self.view_metar_taf_icao1_data)
        self.main_view.app_view.viewICAO1_button.bind(
            '<Return>', self.view_metar_taf_icao1_data)
        self.main_view.app_view.viewICAO2_button.bind(
            '<Button>', self.view_metar_taf_icao2_data)
        self.main_view.app_view.viewICAO2_button.bind(
            '<Return>', self.view_metar_taf_icao2_data)
        self.main_view.app_view.viewICAO3_button.bind(
            '<Button>', self.view_metar_taf_icao3_data)
        self.main_view.app_view.viewICAO3_button.bind(
            '<Return>', self.view_metar_taf_icao3_data)
        self.main_view.app_view.viewICAO4_button.bind(
            '<Button>', self.view_metar_taf_icao4_data)
        self.main_view.app_view.viewICAO4_button.bind(
            '<Return>', self.view_metar_taf_icao4_data)
        self.main_view.app_view.viewICAO5_button.bind(
            '<Button>', self.view_metar_taf_icao5_data)
        self.main_view.app_view.viewICAO5_button.bind(
            '<Return>', self.view_metar_taf_icao5_data)
        self.main_view.app_view.viewICAO6_button.bind(
            '<Button>', self.view_metar_taf_icao6_data)
        self.main_view.app_view.viewICAO6_button.bind(
            '<Return>', self.view_metar_taf_icao6_data)
        self.main_view.app_view.viewICAO7_button.bind(
            '<Button>', self.view_metar_taf_icao7_data)
        self.main_view.app_view.viewICAO7_button.bind(
            '<Return>', self.view_metar_taf_icao7_data)
        self.main_view.app_view.viewICAO8_button.bind(
            '<Button>', self.view_metar_taf_icao8_data)
        self.main_view.app_view.viewICAO8_button.bind(
            '<Return>', self.view_metar_taf_icao8_data)
        self.main_view.app_view.viewICAO9_button.bind(
            '<Button>', self.view_metar_taf_icao9_data)
        self.main_view.app_view.viewICAO9_button.bind(
            '<Return>', self.view_metar_taf_icao9_data)

        """Set the colour state fields to initially all be grey"""
        self.update_fields.set_colourstates_grey(self.main_view)
        self.update_fields.set_icao_fields(self.main_view,
                                           self.restore_icao_list())

    def run(self):
        """Start the application"""
        self.root.title('Diversion Monitor v1.4')
        self.root.deiconify()
        self.root.mainloop()

    def start_monitor(self, event):
        """Start the automatic monitoring of entered ICAOs, initial messages
        are collected and fields updated before setting scheduled checking
        :param event: 'Start Monitoring' button pressed."""
        if not self.monitoring:
            self.main_view.controls_view.monitor_button.configure(
                text='Monitoring...')
            self.data_check_sched()
            self.monitoring = True
            self.check_metars_tafs()
            self.update_display()

    def data_check_sched(self):
        """Set a schedule for collecting and checking for messages from the
        WFS server using a background scheduler."""
        scheduler = BackgroundScheduler()
        trigger = IntervalTrigger(seconds=300)  # check every 5 mins (300msec)
        scheduler.add_job(self.check_metars_tafs, trigger)
        scheduler.start()

    def update_data_now(self, event):
        """Response action for 'Update Now' button press - initiate
        update of QNH/Time fields.
        :param event: 'Update Now' button pressed."""
        self.check_metars_tafs()

    def update_display(self):
        """For each ICAO field, get the ICAO, check for the latest messages
        (METAR/SPECI/TAF) and update the station dictionary with the new data.
        Then update the window fields. Note 'check_metars_tafs() should always
        be called before updating the display to ensure that the latest data
        has been retried from the WFS server"""
        icao0 = self.main_view.app_view.icao0.get()
        icao0_metar_data = get_xml_data.get_latest_metar(icao0)
        icao0_taf_data = get_xml_data.get_latest_taf(icao0)
        self.icao0_data.update_icao_data(icao0,
                                         icao0_metar_data[0],
                                         icao0_metar_data[1],
                                         icao0_taf_data[0],
                                         icao0_taf_data[1],
                                         self.icao0_data.station_dict)
        self.update_fields.update_icao0(self.icao0_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao1_data.station_dict,
                                          self.main_view)

        icao1 = self.main_view.app_view.icao1.get()
        icao1_metar_data = get_xml_data.get_latest_metar(icao1)
        icao1_taf_data = get_xml_data.get_latest_taf(icao1)
        self.icao1_data.update_icao_data(icao1,
                                         icao1_metar_data[0],
                                         icao1_metar_data[1],
                                         icao1_taf_data[0],
                                         icao1_taf_data[1],
                                         self.icao1_data.station_dict)
        self.update_fields.update_icao1(self.icao1_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao1_data.station_dict,
                                          self.main_view)

        icao2 = self.main_view.app_view.icao2.get()
        icao2_metar_data = get_xml_data.get_latest_metar(icao2)
        icao2_taf_data = get_xml_data.get_latest_taf(icao2)
        self.icao2_data.update_icao_data(icao2,
                                         icao2_metar_data[0],
                                         icao2_metar_data[1],
                                         icao2_taf_data[0],
                                         icao2_taf_data[1],
                                         self.icao2_data.station_dict)
        self.update_fields.update_icao2(self.icao2_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao2_data.station_dict,
                                          self.main_view)

        icao3 = self.main_view.app_view.icao3.get()
        icao3_metar_data = get_xml_data.get_latest_metar(icao3)
        icao3_taf_data = get_xml_data.get_latest_taf(icao3)
        self.icao3_data.update_icao_data(icao3,
                                         icao3_metar_data[0],
                                         icao3_metar_data[1],
                                         icao3_taf_data[0],
                                         icao3_taf_data[1],
                                         self.icao3_data.station_dict)
        self.update_fields.update_icao3(self.icao3_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao3_data.station_dict,
                                          self.main_view)

        icao4 = self.main_view.app_view.icao4.get()
        icao4_metar_data = get_xml_data.get_latest_metar(icao4)
        icao4_taf_data = get_xml_data.get_latest_taf(icao4)
        self.icao4_data.update_icao_data(icao4,
                                         icao4_metar_data[0],
                                         icao4_metar_data[1],
                                         icao4_taf_data[0],
                                         icao4_taf_data[1],
                                         self.icao4_data.station_dict)
        self.update_fields.update_icao4(self.icao4_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao4_data.station_dict,
                                          self.main_view)

        icao5 = self.main_view.app_view.icao5.get()
        icao5_metar_data = get_xml_data.get_latest_metar(icao5)
        icao5_taf_data = get_xml_data.get_latest_taf(icao5)
        self.icao5_data.update_icao_data(icao5, icao5_metar_data[0],
                                         icao5_metar_data[1],
                                         icao5_taf_data[0],
                                         icao5_taf_data[1],
                                         self.icao5_data.station_dict)
        self.update_fields.update_icao5(self.icao5_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao5_data.station_dict,
                                          self.main_view)

        icao6 = self.main_view.app_view.icao6.get()
        icao6_metar_data = get_xml_data.get_latest_metar(icao6)
        icao6_taf_data = get_xml_data.get_latest_taf(icao6)
        self.icao6_data.update_icao_data(icao6,
                                         icao6_metar_data[0],
                                         icao6_metar_data[1],
                                         icao6_taf_data[0],
                                         icao6_taf_data[1],
                                         self.icao6_data.station_dict)
        self.update_fields.update_icao6(self.icao6_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao6_data.station_dict,
                                          self.main_view)

        icao7 = self.main_view.app_view.icao7.get()
        icao7_metar_data = get_xml_data.get_latest_metar(icao7)
        icao7_taf_data = get_xml_data.get_latest_taf(icao7)
        self.icao7_data.update_icao_data(icao7,
                                         icao7_metar_data[0],
                                         icao7_metar_data[1],
                                         icao7_taf_data[0],
                                         icao7_taf_data[1],
                                         self.icao7_data.station_dict)
        self.update_fields.update_icao7(self.icao7_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao7_data.station_dict,
                                          self.main_view)

        icao8 = self.main_view.app_view.icao8.get()
        icao8_metar_data = get_xml_data.get_latest_metar(icao8)
        icao8_taf_data = get_xml_data.get_latest_taf(icao8)
        self.icao8_data.update_icao_data(icao8,
                                         icao8_metar_data[0],
                                         icao8_metar_data[1],
                                         icao8_taf_data[0],
                                         icao8_taf_data[1],
                                         self.icao8_data.station_dict)
        self.update_fields.update_icao8(self.icao8_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao8_data.station_dict,
                                          self.main_view)

        icao9 = self.main_view.app_view.icao9.get()
        icao9_metar_data = get_xml_data.get_latest_metar(icao9)
        icao9_taf_data = get_xml_data.get_latest_taf(icao9)
        self.icao9_data.update_icao_data(icao9,
                                         icao9_metar_data[0],
                                         icao9_metar_data[1],
                                         icao9_taf_data[0],
                                         icao9_taf_data[1],
                                         self.icao9_data.station_dict)
        self.update_fields.update_icao9(self.icao9_data.station_dict,
                                        self.main_view)
        self.update_fields.display_alerts(self.icao9_data.station_dict,
                                          self.main_view)

        self.update_fields.display_alerts(self.icao0_data.station_dict,
                                          self.main_view)

        if self.update_fields.status_change:
            self.update_fields.trigger_alert()

    def get_icao_list(self):
        """Get a list of the ICAO's currently entered into the ICAO fields"""
        icao_list = [self.main_view.app_view.icao0.get(),
                     self.main_view.app_view.icao1.get(),
                     self.main_view.app_view.icao2.get(),
                     self.main_view.app_view.icao3.get(),
                     self.main_view.app_view.icao4.get(),
                     self.main_view.app_view.icao5.get(),
                     self.main_view.app_view.icao6.get(),
                     self.main_view.app_view.icao7.get(),
                     self.main_view.app_view.icao8.get(),
                     self.main_view.app_view.icao9.get()]
        return icao_list

    def check_metars_tafs(self):
        """ Get the latest METAR/TAF/SPECI messages for the ICAOs entered"""

        # Get a timestamp for the 'Last check' field
        timestamp = str(datetime.datetime.strftime(datetime.datetime.utcnow(),
                                                   '%d%H%M Z'))
        self.main_view.controls_view.time.set(timestamp)

        get_xml_data.update_report_data(self.main_view.app_view.icao0.get(),
                                        self.main_view.app_view.icao1.get(),
                                        self.main_view.app_view.icao2.get(),
                                        self.main_view.app_view.icao3.get(),
                                        self.main_view.app_view.icao4.get(),
                                        self.main_view.app_view.icao5.get(),
                                        self.main_view.app_view.icao6.get(),
                                        self.main_view.app_view.icao7.get(),
                                        self.main_view.app_view.icao8.get(),
                                        self.main_view.app_view.icao9.get())
        # Now we have latest data, update the display fields
        self.update_display()

    def caps(self, event):
        """Capitalise characters typed into ICAO boxes
        :param event: Keyboard character typed into an ICAO box."""
        self.main_view.app_view.icao0.set(
            self.main_view.app_view.icao0.get().upper())
        self.main_view.app_view.icao1.set(
            self.main_view.app_view.icao1.get().upper())
        self.main_view.app_view.icao2.set(
            self.main_view.app_view.icao2.get().upper())
        self.main_view.app_view.icao3.set(
            self.main_view.app_view.icao3.get().upper())
        self.main_view.app_view.icao4.set(
            self.main_view.app_view.icao4.get().upper())
        self.main_view.app_view.icao5.set(
            self.main_view.app_view.icao5.get().upper())
        self.main_view.app_view.icao6.set(
            self.main_view.app_view.icao6.get().upper())
        self.main_view.app_view.icao7.set(
            self.main_view.app_view.icao7.get().upper())
        self.main_view.app_view.icao8.set(
            self.main_view.app_view.icao8.get().upper())
        self.main_view.app_view.icao9.set(
            self.main_view.app_view.icao9.get().upper())

    @staticmethod
    def restore_icao_list():
        """Retrieves ICAO's from saved file """
        try:
            if os.path.exists('.icao_list.conf'):
                os.system('attrib -h .icao_list.conf')
            with open('.icao_list.conf', 'rb') as icao_restore:
                icao_string = pickle.load(icao_restore)
                os.system('attrib +h .icao_list.conf')
            return icao_string
        except IOError as err:
            print('ICAO list restore file error: ' + str(err))
        except pickle.PickleError as perr:
            print('ICAO list restore pickling error: ' + str(perr))
        except EOFError as eoferr:
            print('ICAO list restore error: ' + str(eoferr))

    def view_metar_taf_icao0_data(self, event):
        """Call display box and populate with latest METAR/TAF when 'view'
        button pressed"""
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao0_data.station_dict['METAR'],
                                  self.icao0_data.station_dict['TAF'],
                                  self.icao0_data.station_dict['ICAO'])

    def view_metar_taf_icao1_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao1_data.station_dict['METAR'],
                                  self.icao1_data.station_dict['TAF'],
                                  self.icao1_data.station_dict['ICAO'])

    def view_metar_taf_icao2_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao2_data.station_dict['METAR'],
                                  self.icao2_data.station_dict['TAF'],
                                  self.icao2_data.station_dict['ICAO'])

    def view_metar_taf_icao3_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao3_data.station_dict['METAR'],
                                  self.icao3_data.station_dict['TAF'],
                                  self.icao3_data.station_dict['ICAO'])

    def view_metar_taf_icao4_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao4_data.station_dict['METAR'],
                                  self.icao4_data.station_dict['TAF'],
                                  self.icao4_data.station_dict['ICAO'])

    def view_metar_taf_icao5_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao5_data.station_dict['METAR'],
                                  self.icao5_data.station_dict['TAF'],
                                  self.icao5_data.station_dict['ICAO'])

    def view_metar_taf_icao6_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao6_data.station_dict['METAR'],
                                  self.icao6_data.station_dict['TAF'],
                                  self.icao6_data.station_dict['ICAO'])

    def view_metar_taf_icao7_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao7_data.station_dict['METAR'],
                                  self.icao7_data.station_dict['TAF'],
                                  self.icao7_data.station_dict['ICAO'])

    def view_metar_taf_icao8_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao8_data.station_dict['METAR'],
                                  self.icao8_data.station_dict['TAF'],
                                  self.icao8_data.station_dict['ICAO'])

    def view_metar_taf_icao9_data(self, event):
        msgbox = MetarTafDialog(self.root)
        msgbox.view_metar_taf_msg(self.icao9_data.station_dict['METAR'],
                                  self.icao9_data.station_dict['TAF'],
                                  self.icao9_data.station_dict['ICAO'])

    def save_icao_list(self):
        """Saves the present ICAO's to a file"""

        try:
            if os.path.exists('.icao_list.conf'):
                os.system('attrib -h .icao_list.conf')
            with open('.icao_list.conf', 'wb') as icaos:
                pickle.dump(self.get_icao_list(), icaos)
                os.system('attrib +h .icao_list.conf')

        except IOError as err:
            print('ICAO list save file error: ' + str(err))
        except pickle.PickleError as perr:
            print('ICAO list save pickling error: ' + str(perr))
        except NameError:
            print('ICAO list undefined')

    def exit_app(self, event):
        self.save_icao_list()
        sys.exit()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
