'''
    Every QR code needs some information to generate the code.
        1. You need to provde some "data", this being the link for script that will be executed when scanned.
        2. You need to provide a path to save the QR code that is generated
        3. You need to provide a parameters to generate the QR code, such as the width and height, and the border size.


    This "main_app.py" file will generate the window to accept input from the user and use that to generate the appropriate QR code.
'''

'''
    This file needs to accept information from the user. That information includes
        1. Name of the saved qr code, DONE
        
        2. A file path of to where to save the code, if applicable DONE
        
        3. The error correction type of the code
        
        4. The size, shape, rotation, and color or the code. Color should include data color, and background color, and border color
        
        5. Whether or not the include a image specified by the user, and insert this image into the center of the QR code. 
        
        6. Finally the link or "data" as to where this code will point too. Should be in the format "https://something.com. Or if the person wants 
        to copy and paste the link directly they can. DONE
        
    Finally, at the bottom of the window the program should update a LIVE redition of the  QR code for the user to see. 
        i.e the color, detail, image insertion, and the rotation. Basically a preview window for the code.
        
'''

import tkinter as tk
from tkinter import messagebox

from main_app_functions import MainAppFunc

# from tkinter import filedialog

funcs = MainAppFunc()

# region Creating the main Window

window = tk.Tk()
window.title('QR Code Generator')
window.geometry('450x300')
# endregion

# region Building the first Frame. This fame will take in the name to save the QR code as
frame_save_name = tk.Frame(master=window)
label_save_name = tk.Label(master=frame_save_name, text='Name of QR Code', padx=10).grid_configure(row=0, column=0)
entry_save_name_VAL = tk.StringVar()
entry_save_name = tk.Entry(master=frame_save_name, textvariable=entry_save_name_VAL).grid_configure(row=0, column=1)
frame_save_name.pack()
# endregion

# region Second Frame: Radion Buttons for declaring the file type to save as
frame_save_file_type = tk.Frame(master=window)
label_save_file_type = tk.Label(master=frame_save_file_type, text="File Type", padx=10).grid_configure(row=0, column=0)
file_type_val = tk.IntVar()
Rb1_png = tk.Radiobutton(master=frame_save_file_type, text='PNG', variable=file_type_val, value=1).grid_configure(row=0, column=1)
Rb2_jpg = tk.Radiobutton(master=frame_save_file_type, text='JPEG', variable=file_type_val, value=2).grid_configure(row=0, column=2)

frame_save_file_type.pack()
# endregion

# region Third Frame: Take in a file path, or select the file path from a button
frame_file_path = tk.Frame(master=window)
label_file_path = tk.Label(master=frame_file_path, text='File path to save QR Code ', padx=10).grid_configure(row=0, column=0)

button_file_path = tk.Button(master=frame_file_path, text='Choose Path', command=lambda: funcs.file_path_grab(entry_file_path_VAL)).grid_configure(
    row=0, column=2)

entry_file_path_VAL = tk.StringVar()
entry_file_path = tk.Entry(master=frame_file_path, textvariable=entry_file_path_VAL).grid_configure(row=0, column=1)

frame_file_path.pack()
# endregion

# region Fourth Frame: This entry will be the link, or data, that the user will input as the data for the qr code to point too
frame_data = tk.Frame(master=window)
label_data = tk.Label(master=frame_data, text='Website (Link) for QR Code to point too', padx=10).grid_configure(row=0, column=0)
entry_data_val = tk.StringVar()
entry_data = tk.Entry(master=frame_data, textvariable=entry_data_val, width=30).grid_configure(row=0, column=1)
entry_data_val.set("Ex : https://google.com")

frame_data.pack()
# endregion


window.protocol(name="WM_DELETE_WINDOW", func=lambda: funcs.on_closing(window=window, msg_box=messagebox))

window.mainloop()
