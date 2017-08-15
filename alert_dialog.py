__author__ = 'Mark Baker  email: mark2182@mac.com'

import dialog_framework
import tkinter as tk


class AlertDialog(dialog_framework.Dialog):
    """Generate user alerts using the dialog framework (provides more flexibility than tcl/tk standard dialog). Two
    methods are used so that the alert windows can be placed at different locations and therefore not be missed"""
    def body(self, master):
        self.alert_msg_field = tk.Label(master)
        self.alert_msg_field.grid(row=1, column=0)
        self.title('Status ALERT')
        return self.alert_msg_field

    def deterioration_alert(self, alert_msg):
        """Generate an user alert message box if an ICAO has gone to a lower colour state"""
        self.geometry("+%d+%d" % (self.parent.winfo_rootx() + 270,
                                  self.parent.winfo_rooty() + 10))

        self.alert_msg_field.configure(text=alert_msg, width=20, padx=8, pady=8)

    def improvement_alert(self, alert_msg):
        """Generate an user alert message box if an ICAO has gone to a higher colour state"""
        self.geometry("+%d+%d" % (self.parent.winfo_rootx() + 70,
                                  self.parent.winfo_rooty() + 10))

        # self.alert_msg_field.configure(text=alert_msg, background="green", foreground="black", width=20, padx=8, pady=8)
        self.alert_msg_field.configure(text=alert_msg, width=20, padx=8, pady=8)
