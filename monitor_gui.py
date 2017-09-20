#!/usr/bin/env python
import sys

if sys.version_info[0] < 3:
    import Tkinter as tk
    import ttk
else:
    import tkinter as tk
    from tkinter import ttk as ttk

__author__ = 'Mark Baker  email: mark2182@mac.com'


class MainView:
    """Main GUI class responsible for initiating separate window frames for the various display elements."""

    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, padx=5, pady=5)
        self.app_view = AppView(master)
        self.controls_view = ControlsView(master)


class AppView:
    """Label window frame containing the widgets for displaying Obs time, latest and previous QNH. """

    def __init__(self, root):
        self.frame_metar_monitor = tk.LabelFrame(root, text='ICAO Selector')
        self.frame_metar_monitor.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        self.icao_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao_label.grid(row=0, column=1, padx=5, pady=5)

        self.dtg_label = ttk.Label(self.frame_metar_monitor, text="Report Time:")
        self.dtg_label.grid(row=0, column=2, padx=5, pady=5)

        self.prev_label = ttk.Label(self.frame_metar_monitor, text="Prev:")
        self.prev_label.grid(row=0, column=3, padx=13, pady=5)

        self.latest_label = ttk.Label(self.frame_metar_monitor, text="Latest:")
        self.latest_label.grid(row=0, column=4, padx=13, pady=5)

        self.status_label = ttk.Label(self.frame_metar_monitor, text="TAF status:")
        self.status_label.grid(row=0, column=5, padx=10, pady=5)

        self.icao0 = tk.StringVar()
        self.icao0_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao0, width=8)
        self.icao0_entry.grid(row=1, column=1, padx=5, pady=5)

        self.icao0_time = tk.StringVar()
        self.icao0_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao0_time)
        self.icao0_time_field.grid(row=1, column=2, padx=5, pady=5)

        self.icao0_prev_colour = tk.StringVar()
        self.icao0_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao0_prev_colour)
        self.icao0_prev_colour_field.grid(row=1, column=3, padx=5, pady=5)

        self.icao0_latest_colour = tk.StringVar()
        self.icao0_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao0_latest_colour)
        self.icao0_latest_colour_field.grid(row=1, column=4, padx=5, pady=5)

        self.icao0_taf_status = tk.StringVar()
        self.icao0_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao0_taf_status)
        self.icao0_taf_status_field.grid(row=1, column=5, padx=5, pady=5)

        self.icao1 = tk.StringVar()
        self.icao1_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao1, width=8)
        self.icao1_entry.grid(row=2, column=1, padx=5, pady=5)

        self.icao1_time = tk.StringVar()
        self.icao1_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao1_time)
        self.icao1_time_field.grid(row=2, column=2, padx=5, pady=5)

        self.icao1_prev_colour = tk.StringVar()
        self.icao1_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao1_prev_colour)
        self.icao1_prev_colour_field.grid(row=2, column=3, padx=5, pady=5)

        self.icao1_latest_colour = tk.StringVar()
        self.icao1_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao1_latest_colour)
        self.icao1_latest_colour_field.grid(row=2, column=4, padx=5, pady=5)

        self.icao1_taf_status = tk.StringVar()
        self.icao1_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao1_taf_status)
        self.icao1_taf_status_field.grid(row=2, column=5, padx=5, pady=5)

        self.icao2 = tk.StringVar()
        self.icao2_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao2, width=8)
        self.icao2_entry.grid(row=3, column=1, padx=5, pady=5)

        self.icao2_time = tk.StringVar()
        self.icao2_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao2_time)
        self.icao2_time_field.grid(row=3, column=2, padx=5, pady=5)

        self.icao2_prev_colour = tk.StringVar()
        self.icao2_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao2_prev_colour)
        self.icao2_prev_colour_field.grid(row=3, column=3, padx=5, pady=5)

        self.icao2_latest_colour = tk.StringVar()
        self.icao2_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao2_latest_colour)
        self.icao2_latest_colour_field.grid(row=3, column=4, padx=5, pady=5)

        self.icao2_taf_status = tk.StringVar()
        self.icao2_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao2_taf_status)
        self.icao2_taf_status_field.grid(row=3, column=5, padx=5, pady=5)

        self.icao3 = tk.StringVar()
        self.icao3_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao3, width=8)
        self.icao3_entry.grid(row=4, column=1, padx=5, pady=5)

        self.icao3_time = tk.StringVar()
        self.icao3_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao3_time)
        self.icao3_time_field.grid(row=4, column=2, padx=5, pady=5)

        self.icao3_prev_colour = tk.StringVar()
        self.icao3_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao3_prev_colour)
        self.icao3_prev_colour_field.grid(row=4, column=3, padx=5, pady=5)

        self.icao3_latest_colour = tk.StringVar()
        self.icao3_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao3_latest_colour)
        self.icao3_latest_colour_field.grid(row=4, column=4, padx=5, pady=5)

        self.icao3_taf_status = tk.StringVar()
        self.icao3_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao3_taf_status)
        self.icao3_taf_status_field.grid(row=4, column=5, padx=5, pady=5)

        self.icao4 = tk.StringVar()
        self.icao4_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao4, width=8)
        self.icao4_entry.grid(row=5, column=1, padx=5, pady=5)

        self.icao4_time = tk.StringVar()
        self.icao4_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao4_time)
        self.icao4_time_field.grid(row=5, column=2, padx=5, pady=5)

        self.icao4_prev_colour = tk.StringVar()
        self.icao4_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao4_prev_colour)
        self.icao4_prev_colour_field.grid(row=5, column=3, padx=5, pady=5)

        self.icao4_latest_colour = tk.StringVar()
        self.icao4_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao4_latest_colour)
        self.icao4_latest_colour_field.grid(row=5, column=4, padx=5, pady=5)

        self.icao4_taf_status = tk.StringVar()
        self.icao4_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao4_taf_status)
        self.icao4_taf_status_field.grid(row=5, column=5, padx=5, pady=5)

        self.icao5 = tk.StringVar()
        self.icao5_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao5, width=8)
        self.icao5_entry.grid(row=6, column=1, padx=5, pady=5)

        self.icao5_time = tk.StringVar()
        self.icao5_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao5_time)
        self.icao5_time_field.grid(row=6, column=2, padx=5, pady=5)

        self.icao5_prev_colour = tk.StringVar()
        self.icao5_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao5_prev_colour)
        self.icao5_prev_colour_field.grid(row=6, column=3, padx=5, pady=5)

        self.icao5_latest_colour = tk.StringVar()
        self.icao5_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao5_latest_colour)
        self.icao5_latest_colour_field.grid(row=6, column=4, padx=5, pady=5)

        self.icao5_taf_status = tk.StringVar()
        self.icao5_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao5_taf_status)
        self.icao5_taf_status_field.grid(row=6, column=5, padx=5, pady=5)

        self.icao6 = tk.StringVar()
        self.icao6_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao6, width=8)
        self.icao6_entry.grid(row=7, column=1, padx=5, pady=5)

        self.icao6_time = tk.StringVar()
        self.icao6_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao6_time)
        self.icao6_time_field.grid(row=7, column=2, padx=5, pady=5)

        self.icao6_prev_colour = tk.StringVar()
        self.icao6_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao6_prev_colour)
        self.icao6_prev_colour_field.grid(row=7, column=3, padx=5, pady=5)

        self.icao6_latest_colour = tk.StringVar()
        self.icao6_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao6_latest_colour)
        self.icao6_latest_colour_field.grid(row=7, column=4, padx=5, pady=5)

        self.icao6_taf_status = tk.StringVar()
        self.icao6_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao6_taf_status)
        self.icao6_taf_status_field.grid(row=7, column=5, padx=5, pady=5)

        self.icao7 = tk.StringVar()
        self.icao7_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao7, width=8)
        self.icao7_entry.grid(row=8, column=1, padx=5, pady=5)

        self.icao7_time = tk.StringVar()
        self.icao7_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao7_time)
        self.icao7_time_field.grid(row=8, column=2, padx=5, pady=5)

        self.icao7_prev_colour = tk.StringVar()
        self.icao7_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao7_prev_colour)
        self.icao7_prev_colour_field.grid(row=8, column=3, padx=5, pady=5)

        self.icao7_latest_colour = tk.StringVar()
        self.icao7_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao7_latest_colour)
        self.icao7_latest_colour_field.grid(row=8, column=4, padx=5, pady=5)

        self.icao7_taf_status = tk.StringVar()
        self.icao7_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao7_taf_status)
        self.icao7_taf_status_field.grid(row=8, column=5, padx=5, pady=5)

        self.icao8 = tk.StringVar()
        self.icao8_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao8, width=8)
        self.icao8_entry.grid(row=9, column=1, padx=5, pady=5)

        self.icao8_time = tk.StringVar()
        self.icao8_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao8_time)
        self.icao8_time_field.grid(row=9, column=2, padx=5, pady=5)

        self.icao8_prev_colour = tk.StringVar()
        self.icao8_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao8_prev_colour)
        self.icao8_prev_colour_field.grid(row=9, column=3, padx=5, pady=5)

        self.icao8_latest_colour = tk.StringVar()
        self.icao8_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao8_latest_colour)
        self.icao8_latest_colour_field.grid(row=9, column=4, padx=5, pady=5)

        self.icao8_taf_status = tk.StringVar()
        self.icao8_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao8_taf_status)
        self.icao8_taf_status_field.grid(row=9, column=5, padx=5, pady=5)

        self.icao9 = tk.StringVar()
        self.icao9_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao9, width=8)
        self.icao9_entry.grid(row=10, column=1, padx=5, pady=5)

        self.icao9_time = tk.StringVar()
        self.icao9_time_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao9_time)
        self.icao9_time_field.grid(row=10, column=2, padx=5, pady=5)

        self.icao9_prev_colour = tk.StringVar()
        self.icao9_prev_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao9_prev_colour)
        self.icao9_prev_colour_field.grid(row=10, column=3, padx=5, pady=5)

        self.icao9_latest_colour = tk.StringVar()
        self.icao9_latest_colour_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao9_latest_colour)
        self.icao9_latest_colour_field.grid(row=10, column=4, padx=5, pady=5)

        self.icao9_taf_status = tk.StringVar()
        self.icao9_taf_status_field = ttk.Label(self.frame_metar_monitor, textvariable=self.icao9_taf_status)
        self.icao9_taf_status_field.grid(row=10, column=5, padx=5, pady=5)

        self.viewICAO0_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO0_button.grid(row=1, column=0, padx=5, pady=5)

        self.viewICAO1_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO1_button.grid(row=2, column=0, padx=5, pady=5)

        self.viewICAO2_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO2_button.grid(row=3, column=0, padx=5, pady=5)

        self.viewICAO3_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO3_button.grid(row=4, column=0, padx=5, pady=5)

        self.viewICAO4_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO4_button.grid(row=5, column=0, padx=5, pady=5)

        self.viewICAO5_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO5_button.grid(row=6, column=0, padx=5, pady=5)

        self.viewICAO6_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO6_button.grid(row=7, column=0, padx=5, pady=5)

        self.viewICAO7_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO7_button.grid(row=8, column=0, padx=5, pady=5)

        self.viewICAO8_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO8_button.grid(row=9, column=0, padx=5, pady=5)

        self.viewICAO9_button = ttk.Button(self.frame_metar_monitor, text='View', width=8)
        self.viewICAO9_button.grid(row=10, column=0, padx=5, pady=5)


class ControlsView:
    """ GUI elements - monitoring, update and exit buttons"""
    def __init__(self, root):

        self.frame_controls = ttk.Frame(root)
        self.frame_controls.grid(row=2, columnspan=9, padx=5, pady=5)

        self.monitor_button = ttk.Button(self.frame_controls, text='Start Monitor', width=14)
        self.monitor_button.grid(sticky=tk.W, row=0, column=0, padx=5, pady=5)

        self.time_label = ttk.Label(self.frame_controls, text="Last Check:", anchor=tk.E)
        self.time_label.grid(row=0, column=2, columnspan=1, padx=5, pady=5)

        self.time = tk.StringVar()
        self.time_result = ttk.Label(self.frame_controls, textvariable=self.time, width=8, anchor=tk.W)
        self.time_result.grid(row=0, column=3, columnspan=1, padx=5, pady=5)

        self.update_data_button = ttk.Button(self.frame_controls, text='Update Now', width=13)
        self.update_data_button.grid(sticky=tk.E, row=0, column=8, padx=5, pady=5)

        self.exit_button = ttk.Button(self.frame_controls, text='Exit')
        self.exit_button.grid(sticky=tk.E, row=0, column=9, padx=5, pady=5)

