import qrcode as qr
import tkinter as tk

def gen():
    img = qr.make(e.get())
    img.save(f"QrCode.png")
    my_window.destroy()


my_window = tk.Tk();
my_window.geometry("400x300");
my_window.title('Qr Code Generator');

l=tk.Label(my_window,text='Enter URL: ',font=100,fg="black")
l.grid(row=1,column=0,padx=10,pady=10)


e = tk.Entry(my_window, font=20, bg='lightyellow')
e.grid(row=1, column=1, padx=10, pady=3)
b1=tk.Button(my_window,text='Submit', bg='lightgreen',command=lambda: gen(),font=18)
b1.grid(row=2,column=0,padx=10,pady=20)

my_window.mainloop()


