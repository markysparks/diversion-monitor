import dialog_framework
import tkinter as tk
from tkinter import ttk as ttk

__author__ = 'Mark Baker  email: mark2182@mac.com'


class MetarTafDialog(dialog_framework.Dialog):
    """Tools to display METAR/TAF messages in a window box using the
    dialog framework"""
    def body(self, master):
        ttk.Label(master, text="METAR/SPECI:").grid(row=0,
                                                    sticky=tk.W, pady=5)
        ttk.Label(master, text="TAF:").grid(row=2, sticky=tk.W, pady=5)

        self.metar_msg_field = tk.Text(master, height=3, wrap="word",
                                       background="cyan", width=75)
        self.taf_msg_field = tk.Text(master, height=4, wrap="word", width=75)

        self.metar_msg_field.grid(row=1, column=0)
        self.taf_msg_field.grid(row=3, column=0)
        # return self.body  # initial focus if required

    def apply(self):
        first = int(self.metar_msg_field.get())
        second = int(self.taf_msg_field.get())
        print(first, second)  # or something

    def view_metar_taf_msg(self, metar_msg, taf_msg, icao):
        self.title('Latest METAR & TAF   ' + icao)

        metar_str = str(metar_msg)
        taf_str = str(taf_msg)

        self.metar_msg_field.insert(tk.INSERT, metar_str)
        self.metar_msg_field.pack

        self.taf_msg_field.insert(tk.INSERT, taf_str)
        self.taf_msg_field.pack
