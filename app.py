import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor

import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


import segno
from PIL import Image


def hex_to_rgb(hex: str):
    hex = hex[1:]
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i + 2], 16)
        rgb.append(decimal)
    return tuple(rgb)

'''
#todo implement a function to determine the appropriate distance between buttons, entries, and labels. 
'''
global my_img


class UpdatedWindow:
    def __init__(self, win):
        self.insert_image = None
        self.win = win
        self.cond = 0

        self.ecc = [
            "L -> 7%",
            "M -> 15%",
            "Q -> 25%",
            "H -> 30%"
        ]

        self.qrcode_color = "#000000"
        self.qrcode_Border_Color = "#FFFFFF"
        self.qrcode_Background_Color = "#FFFFFF"

        self.qrcode = QRCODE()
        self.qrcode.__int__()

        self.code_name_FRAME = CTkFrame(master=win).grid_configure(row=0, column=0)
        self.code_name_LABEL = CTkLabel(master=self.code_name_FRAME, text="Name of QR Code")
        self.code_name_ENTRY = CTkEntry(master=win)


        self.file_type_LABEL = CTkLabel(master=win, text="File Type")
        self.file_type_VAL = IntVar()
        self.file_type_RB1 = CTkRadioButton(master=win, text="PNG", variable=self.file_type_VAL, value=1)
        self.file_type_RB2 = CTkRadioButton(master=win, text="JPEG", variable=self.file_type_VAL, value=2)


        self.save_file_path_LABEL = CTkLabel(master=win, text="File path to save QR Code")
        self.save_file_path_VAL = StringVar()
        self.save_file_path_ENTRY = CTkEntry(master=win, textvariable=self.save_file_path_VAL)
        self.save_file_path_BUTTON = CTkButton(master=win, text='Save Path', command=lambda: self.grab_save_path())

        self.data_LABEL = CTkLabel(master=win, text='Website to link QR Code')
        self.data_VAL = StringVar()
        self.data_ENTRY = CTkEntry(master=win,textvariable=self.data_VAL)

        self.preview_BUTTON = CTkButton(master=win, text='Preview', command=lambda: self.preview_code())

        self.preview_color_VAL = StringVar()
        self.preview_color_ENTRY = CTkEntry(master=win, textvariable=self.preview_color_VAL,width=100)
        self.preview_color_ENTRY.insert(0, self.qrcode_color)
        self.preview_color_BUTTON = CTkButton(master=win, text='Color',
                                           command=lambda: self.select_color(name="QRCode Color",
                                                                             entry=self.preview_color_ENTRY))

        self.preview_color_border_VAL = StringVar()
        self.preview_color_border_ENTRY = CTkEntry(master=win, textvariable=self.preview_color_border_VAL,width=100)
        self.preview_color_border_ENTRY.insert(0, self.qrcode_Border_Color)

        self.preview_color_border_BUTTON = CTkButton(master=win, text='Border Color',
                                                  command=lambda: self.select_color(name="QRCode Boarder Color",
                                                                                    entry=self.preview_color_border_ENTRY))
        self.preview_color_background_VAL = StringVar()
        self.preview_color_background_ENTRY = CTkEntry(master=win, textvariable=self.preview_color_background_VAL,
                                                    width=100)
        self.preview_color_background_ENTRY.insert(0, self.qrcode_Background_Color)
        self.preview_color_background_BUTTON = CTkButton(master=win, text='Background Color',
                                                      command=lambda: self.select_color(name="QRCode Background Color",
                                                                                        entry=self.preview_color_background_ENTRY))

        self.insert_image_LABEL = CTkLabel(master=win, text='Insert Image')
        self.insert_image_VAL = StringVar()
        self.insert_image_ENTRY = CTkEntry(master=win, textvariable=self.insert_image_VAL, width=100)
        self.insert_image_BUTTON = CTkButton(master=win, text='Choose', command=lambda: self.select_insert_image(), width=40)

        self.box_size_LABEL = CTkLabel(master=win, text='Box Size')
        self.box_size_VAL = IntVar()
        self.box_size_ENTRY = CTkEntry(master=win, textvariable=self.box_size_VAL, width=10)

        self.ecc_LABEL = CTkLabel(master=win, text='Error Correction')
        self.ecc_VAL = StringVar()
        self.ecc_VAL.set(self.qrcode.ecc[0])
        self.ecc_OPTIONS = CTkOptionMenu(master=win, variable=self.ecc_VAL, values=self.qrcode.ecc)

        self.preview_qrcode_LABEL = CTkLabel(master=win, text="QR Code Preview Display Here")
        self.preview_qrcode_obj = CTkLabel(master=win, text="")

        self.save_code_BUTTON = CTkButton(master=win, text='Save QR Code', command=lambda: self.save_qr_code())

        self.code_name_LABEL.place(x=50, y=50)
        self.code_name_ENTRY.place(x=160, y=50)

        self.file_type_LABEL.place(x=320, y=50)
        self.file_type_RB1.place(x=380, y=50)
        self.file_type_RB2.place(x=440, y=50)

        self.save_file_path_LABEL.place(x=11, y=80)
        self.save_file_path_ENTRY.place(x=160, y=80)
        self.save_file_path_BUTTON.place(x=320, y=80)

        self.data_LABEL.place(x=17, y=110)
        self.data_ENTRY.place(x=160, y=110)

        self.preview_BUTTON.place(x=60, y=145)
        self.preview_color_BUTTON.place(x=20, y=200)
        self.preview_color_ENTRY.place(x=170, y=200)

        self.preview_color_border_BUTTON.place(x=20, y=230)
        self.preview_color_border_ENTRY.place(x=170, y=230)

        self.preview_color_background_BUTTON.place(x=20, y=260)
        self.preview_color_background_ENTRY.place(x=170, y=260)

        self.insert_image_LABEL.place(x=20, y=290)
        self.insert_image_ENTRY.place(x=130, y=290)
        self.insert_image_BUTTON.place(x=240, y=290)

        self.ecc_LABEL.place(x=20, y=320)
        self.ecc_OPTIONS.place(x=130, y=320)

        self.preview_qrcode_LABEL.place(x=300, y=170)
        self.preview_qrcode_obj.place(x=300, y=190)

        self.save_code_BUTTON.place(x=60, y=350)

    def grab_save_path(self):
        curr_dir = filedialog.askdirectory()
        self.save_file_path_ENTRY.delete(0, END)
        self.save_file_path_ENTRY.insert(0, curr_dir)
        return

    def preview_code(self):
        global my_img

        qrcode_data = self.data_ENTRY.get()

        data_color = self.preview_color_ENTRY.get()
        border_color = self.preview_color_border_ENTRY.get()
        background_color = self.preview_color_background_ENTRY.get()
        ecc = self.ecc_VAL.get().split(" ")[0]

        if qrcode_data == "":
            return

        while True:
            try:
                self.qrcode.create_code(data=qrcode_data,
                                        err=ecc,
                                        name="tmp",
                                        path="./",
                                        filetype='png',
                                        scale=7,
                                        border_width=5,
                                        background_color=hex_to_rgb(background_color),
                                        border_color=hex_to_rgb(border_color),
                                        data_color=hex_to_rgb(data_color)
                                        )
                tmp_img_save_path = "./tmp.png"
                if self.insert_image_ENTRY.get() == "":
                    img = Image.open(tmp_img_save_path)
                    img = img.convert("RGBA")
                    img.save("path", "PNG")
                    my_img = PhotoImage(file="path")
                    self.preview_qrcode_obj.configure(image=my_img)
                    os.remove("./path")

                else:

                    self.qrcode.insert_custom_image(qr_code_path=tmp_img_save_path,
                                                    image_path=self.insert_image_ENTRY.get())
                    my_img = PhotoImage(file=tmp_img_save_path)

                    self.preview_qrcode_obj.configure(image=my_img)  # Show the qr code in Label
                os.remove(tmp_img_save_path)
                break
            except:
                raise ValueError()

    def select_insert_image(self):
        self.insert_image = filedialog.askopenfile()
        self.insert_image_ENTRY.delete(0, END)
        self.insert_image_ENTRY.insert(0, self.insert_image.name)
        return

    @staticmethod
    def select_color(name: str, entry):
        colors = askcolor(title=name)
        entry.delete(0, END)
        entry.insert(0, colors[1])

    def save_qr_code(self):

        qrcode_data = self.data_ENTRY.get()
        qrcode_name = self.code_name_ENTRY.get()
        qrcode_save_path = self.save_file_path_ENTRY.get()

        data_color = self.preview_color_ENTRY.get()
        border_color = self.preview_color_border_ENTRY.get()
        background_color = self.preview_color_background_ENTRY.get()
        ecc = self.ecc_VAL.get().split(" ")[0]

        if qrcode_data == "":
            messagebox.showerror("Python Error", "Please provide a valid website link (ie 'https://google.com')")
            return
        if qrcode_name == "":
            messagebox.showerror("Python Error", "Please provide a name to save the QR Code as")
            return
        if qrcode_save_path == "":
            messagebox.showerror("Python Error", "Please provide a file path to save the QR Code at")

        try:

            if self.insert_image_ENTRY.get() != "":
                self.qrcode.create_code(data=qrcode_data,
                                        err=ecc,
                                        name=qrcode_name,
                                        path=qrcode_save_path,
                                        filetype='png' if self.file_type_VAL.get() == 1 else 'jpg',
                                        scale=5,
                                        border_width=10,
                                        background_color=hex_to_rgb(background_color),
                                        border_color=hex_to_rgb(border_color),
                                        data_color=hex_to_rgb(data_color),
                                        insert_image=True,
                                        image_path=self.insert_image_ENTRY.get()
                                        )
            else:
                self.qrcode.create_code(data=qrcode_data,
                                        err=ecc,
                                        name=qrcode_name,
                                        path=qrcode_save_path,
                                        filetype='png' if self.file_type_VAL.get() == 1 else 'jpg',
                                        scale=5,
                                        border_width=10,
                                        background_color=hex_to_rgb(background_color),
                                        border_color=hex_to_rgb(border_color),
                                        data_color=hex_to_rgb(data_color)
                                        )



        except:
            messagebox.showerror("Something went wrong. Please make sure all entry's are valid in form and try again")





class QRCODE:
    def __int__(self):
        self.qr_code_versions = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]

        self.ecc = [
            "L -> 7%",
            "M -> 15%",
            "Q -> 25%",
            "H -> 30%"
        ]

    def create_code(self, data: str, err: str, name: str, path: str, filetype: str, scale: int, border_width: int,
                    background_color: tuple[int, ...], border_color: tuple[int, ...], data_color: tuple[int, ...],
                    insert_image=False, image_path=None):
        if str.lower(filetype) == 'png' or str.lower(filetype) == 'jpg' or str.lower(filetype) == 'jpeg':
            qr_code = segno.make_qr(content=data, error=err)
            qr_code.save(
                out=f"{path}/{name}.{filetype}",
                scale=scale,
                border=border_width,
                light=background_color,
                quiet_zone=border_color,
                dark=data_color
            )

            if insert_image:
                self.insert_custom_image(qr_code_path=f"{path}/{name}.{filetype}", image_path=image_path)
        else:
            raise ValueError()

    def insert_custom_image(self, qr_code_path, image_path):
        im = Image.open(qr_code_path)
        im = im.convert("RGBA")
        logo = Image.open(image_path)

        qr_shape = Image.open(qr_code_path).size

        qr_mid_x = qr_shape[0] // 2
        qr_mid_y = qr_shape[1] // 2

        slices_x = qr_shape[0] // 11
        slices_y = qr_shape[1] // 11

        box = (qr_mid_x - slices_x, qr_mid_y - slices_y, qr_mid_x + slices_x, qr_mid_y + slices_y)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region, box)
        im.save(qr_code_path, "PNG")


def main():
    # window = Tk()
    # mywin = MyWindow(window)
    # window.title('Hello Python')
    # window.geometry("650x500+10+10")
    # window.mainloop()
    #----------------------------
    window = CTk()
    mywin = UpdatedWindow(window)
    window.title("Hello Python")
    window.geometry("650x500+10+10")
    window.mainloop()




if __name__ == '__main__':
    main()
