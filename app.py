from tkinter import *
from tkinter import filedialog

import pyqrcode
from PIL import Image


class MyWindow:
    def __init__(self, win):
        self.insert_image = None
        self.win = win
        self.cond = 0
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

        self.code_name_FRAME = Frame(master=win).grid_configure(row=0, column=0)
        self.code_name_LABEL = Label(master=self.code_name_FRAME, text="Name of QR Code")
        self.code_name_ENTRY = Entry(master=win, bd=3)

        self.file_type_LABEL = Label(master=win, text="File Type")
        self.file_type_VAL = IntVar()
        self.file_type_RB1 = Radiobutton(master=win, text="PNG", variable=self.file_type_VAL, value=1)
        self.file_type_RB2 = Radiobutton(master=win, text="JPEG", variable=self.file_type_VAL, value=2)

        self.save_file_path_LABEL = Label(master=win, text="File path to save QR Code")
        self.save_file_path_VAL = StringVar()
        self.save_file_path_ENTRY = Entry(master=win, bd=3, textvariable=self.save_file_path_VAL)
        self.save_file_path_BUTTON = Button(master=win, text='Save Path', command=lambda: self.grab_save_path())

        self.data_LABEL = Label(master=win, text='Website to link QR Code')
        self.data_VAL = StringVar()
        self.data_ENTRY = Entry(master=win, bd=3, textvariable=self.data_VAL)

        self.preview_BUTTON = Button(master=win, text='Preview', command=lambda: self.preview_code())
        self.preview_color_VAL = StringVar()
        self.preview_color_ENTRY = Entry(master=win, textvariable=self.preview_color_VAL, bd=3, width=10)
        self.preview_color_ENTRY.insert(0, "#FFFFFF")
        self.preview_color_LABEL = Label(master=win, text='Color')

        self.preview_color_border_VAL = StringVar()
        self.preview_color_border_ENTRY = Entry(master=win, textvariable=self.preview_color_border_VAL, bd=3, width=10)
        self.preview_color_border_ENTRY.insert(0, "#FFFFFF")
        self.preview_color_border_LABEL = Label(master=win, text='Border Color')

        self.preview_color_background_VAL = StringVar()
        self.preview_color_background_ENTRY = Entry(master=win, textvariable=self.preview_color_background_VAL, bd=3, width=10)
        self.preview_color_background_ENTRY.insert(0, "#FFFFFF")
        self.preview_color_background_LABEL = Label(master=win, text='Background Color')

        self.insert_image_LABEL = Label(master=win, text='Insert Image')
        self.insert_image_VAL = StringVar()
        self.insert_image_ENTRY = Entry(master=win, textvariable=self.insert_image_VAL, bd=3, width=10)
        self.insert_image_BUTTON = Button(master=win, text='Choose', command=lambda: self.select_insert_image())

        self.box_size_LABEL = Label(master=win, text='Box Size')
        self.box_size_VAL = IntVar()
        self.box_size_ENTRY = Entry(master=win, textvariable=self.box_size_VAL, bd=3, width=10)

        self.version_LABEL = Label(master=win, text='QR Code Version')
        self.version_VAL = StringVar()
        self.version_VAL.set(self.qr_code_versions[0])
        self.version_OPTIONS = OptionMenu(win, self.version_VAL, *self.qr_code_versions)

        self.ecc_LABEL = Label(master=win, text='Error Correction')
        self.ecc_VAL = StringVar()
        self.ecc_VAL.set(self.ecc[0])
        self.ecc_OPTIONS = OptionMenu(win, self.ecc_VAL, *self.ecc)

        self.preview_qrcode_LABEL = Label(master=win, text="QR Code Preview Display Here")
        self.preview_qrcode_obj = Label(master=win, text="")

        self.code_name_LABEL.place(x=50, y=50)
        self.code_name_ENTRY.place(x=160, y=50)

        self.file_type_LABEL.place(x=300, y=50)
        self.file_type_RB1.place(x=360, y=50)
        self.file_type_RB2.place(x=410, y=50)

        self.save_file_path_LABEL.place(x=11, y=80)
        self.save_file_path_ENTRY.place(x=160, y=80)
        self.save_file_path_BUTTON.place(x=300, y=80)

        self.data_LABEL.place(x=17, y=110)
        self.data_ENTRY.place(x=160, y=110)

        self.preview_BUTTON.place(x=60, y=130)
        self.preview_color_LABEL.place(x=20, y=170)
        self.preview_color_ENTRY.place(x=130, y=170)

        self.preview_color_border_LABEL.place(x=20, y=200)
        self.preview_color_border_ENTRY.place(x=130, y=200)

        self.preview_color_background_LABEL.place(x=20, y=230)
        self.preview_color_background_ENTRY.place(x=130, y=230)

        self.insert_image_LABEL.place(x=20, y=260)
        self.insert_image_ENTRY.place(x=130, y=260)
        self.insert_image_BUTTON.place(x=200, y=260)

        self.ecc_LABEL.place(x=20, y=290)
        self.ecc_OPTIONS.place(x=130, y=290)

        self.preview_qrcode_LABEL.place(x=300, y=170)
        self.preview_qrcode_obj.place(x=300, y=190)

    def grab_save_path(self):
        curr_dir = filedialog.askdirectory()
        self.save_file_path_ENTRY.delete(0, END)
        self.save_file_path_ENTRY.insert(0, curr_dir)
        return

    def preview_code(self):
        global my_img

        qrcode_data = self.data_ENTRY.get()
        qrcode_name = self.code_name_ENTRY.get()

        data_color = self.preview_color_ENTRY.get()
        border_color = self.preview_color_border_ENTRY.get()
        background_color = self.preview_color_background_ENTRY.get()
        version = self.version_VAL.get()
        ecc = self.ecc_VAL.get().split(" ")[0]
        print(qrcode_data)

        if qrcode_data == "":
            qrcode_data = "https://google.com"

        while True:
            if self.insert_image_ENTRY.get() == "":

                my_qr = pyqrcode.create(qrcode_data, error=ecc)
                my_qr = my_qr.xbm(scale=5)
                my_img = BitmapImage(data=my_qr, background=background_color, foreground=data_color)
                self.preview_qrcode_obj.config(image=my_img)
                break
            else:

                my_qr = pyqrcode.QRCode(qrcode_data, error=ecc)
                my_qr.png("./tmp.png", scale=10, module_color=self.hex_to_rgb(hex=data_color), background=self.hex_to_rgb(hex=background_color))

                im = Image.open("./tmp.png")
                im = im.convert("RGBA")
                logo = Image.open(self.insert_image_ENTRY.get())
                box = (90, 150, 250, 170)
                im.crop(box)
                region = logo
                region = region.resize((box[2] - box[0], box[3] - box[1]))
                im.paste(region, box)
                im.show()  # display in console
                im.save("path", "PNG")
                my_img = PhotoImage(file="path")
                self.preview_qrcode_obj.config(image=my_img)  # Show the qr code in Label
            # except:
            #     self.insert_image_ENTRY.delete(0)
            #     pass



    def select_insert_image(self):
        self.insert_image = filedialog.askopenfile()
        self.insert_image_ENTRY.delete(0, END)
        self.insert_image_ENTRY.insert(0, self.insert_image.name)
        return

    def hex_to_rgb(self, hex):
        hex = hex[1:]
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i + 2], 16)
            rgb.append(decimal)
        return tuple(rgb)



window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("500x400+10+10")
window.mainloop()
