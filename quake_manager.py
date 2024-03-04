from tkinter import *
import time
def click():
    print("1")
    window.destroy()
    time.sleep(3)
    tıkdow = Tk()
    yazi = Label(text="NEDEN TIKLADIN!")
    yazi.pack()
    soru = Label(text="Cevap?")
    yazcakyer = Entry()
    soru.pack()
    yazcakyer.pack()
    gonder = Button(tıkdow, text="gönder")
    gonder.config(command=gonder)
    gonder.pack()
    tıkdow.mainloop()




window = Tk()
button = Button(window,text="Bana tıkla")
button.config(command=click)
button.pack()
window.mainloop()






