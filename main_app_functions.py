'''
    This file is dedicated to incorporating the tkinter functions, and functionality, of the app. That being what the buttons, entry fields,
    and other information is stored as and where. This file will also include the function that is repsonsibile for calling the qrcode_generator.py
    file that will contain the functionality for generating the qr code directly.
'''

from tkinter import filedialog


class MainAppFunc:

    def __int__(self):
        pass

    def file_path_grab(self, entry_val):
        entry_val.set(filedialog.askdirectory())

    def on_closing(self, window, msg_box):
        if msg_box.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
