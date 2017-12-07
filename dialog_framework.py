__author__ = 'Mark Baker  email: mark2182@mac.com'

import tkinter as tk
from tkinter import ttk as ttk


class Dialog(tk.Toplevel):
    """Framework that's used for generating user alerts - provides more
    control over standard tcl/tk alert windows such as size, position and
    focus as well as allowing message checking etc. to continue in the
    background whilst the is active alert.
    See http://www.effbot.org/tkinterbook/tkinter-dialog-windows.htm
    for more info and description"""
    def __init__(self, parent, title=None):

        tk.Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx() + 400,
                                  parent.winfo_rooty() + 5))

        self.initial_focus.focus_set()

        """Following would block application execution until dialog actioned
         - may or may not be required"""
        # self.wait_window(self)

    #
    # Construction hooks

    def body(self, master):
        # Create dialog body. Return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # Add standard button box. override if you don't want the
        # standard buttons

        box = tk.Frame(self)

        # w = ttk.Button(box, text="OK", width=10, command=self.ok,
        # default=tk.ACTIVE)
        # w.pack(side=ttk.LEFT, padx=5, pady=5)
        w = ttk.Button(box, text="Close", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # Standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set()  # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1  # override

    def apply(self):

        pass  # override
