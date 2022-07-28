import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image


def qrcodegenerator(text, name_of_QRcode):
    url = pyqrcode.create(text)
    url.svg(name_of_QRcode + ".svg", scale=8)
    url.png(name_of_QRcode + ".png", scale=6)


def gui():
    tk = Tk()
    tk.configure(background='black')
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    tk.maxsize(800, 800)
    tk.minsize(800, 800)
    tk.title("QRcode Generator")
    heading_label = Label(tk, text="QRcode Generator", relief=GROOVE, foreground="white",
                          background="indigo", padx=10, pady=5, borderwidth=30)
    heading_label.pack(fill=X)

    data = StringVar()
    text_entry = Entry(tk, textvariable=data, relief=GROOVE, background="darkblue", foreground="yellow", borderwidth=10)
    text_entry.place(x=300, y=150)
    data_nameofqrcode = StringVar()
    text_entry2 = Entry(tk, textvariable=data_nameofqrcode, relief=GROOVE, background="darkblue", foreground="yellow",
                        borderwidth=10)
    text_entry2.place(x=300, y=250)

    def gui_to_main():
        qrcodegenerator(data.get(), data_nameofqrcode.get())
        image1 = Image.open(data_nameofqrcode.get() + ".png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.place(x=300, y=500)

        def detroy_QRCODE():
            label1.destroy()
            cancel_btn.destroy()
            text_entry.delete(0, END)
            text_entry2.delete(0, END)

        cancel_btn = Button(tk, text="Close", fg='green', command=detroy_QRCODE, height=2, width=10, background="green")
        cancel_btn.place(x=350, y=450)

    dcr = Button(tk, text="Save And Create", fg='green', command=gui_to_main, height=2, width=15, background="green")
    dcr.place(x=320, y=350)

    def close_window():
        tk.destroy()

    dcr = Button(tk, text="Close Window", fg='green', command=close_window, height=2, width=15, bg="green")
    dcr.pack(side=BOTTOM)
    tk.mainloop()


# qrcodegenerator(data1, data2)


gui()
