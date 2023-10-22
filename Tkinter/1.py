from tkinter import *

root = Tk()    
root.geometry("300x200")  
frame = Frame(root)

def chng_bg_r(b1):
    frame.config(background="red")

def chng_bg_b(b2):
    frame.config(background="blue")

def chng_bg_g(b3):
    frame.config(background="green")

b1 = Button(frame, text = "Red", command = lambda : chng_bg_r(b1), activeforeground = "red",activebackground = "yellow", height=2, width=10)
b2 = Button(frame, text = "Blue", command = lambda : chng_bg_b(b2), activeforeground = "blue",activebackground = "yellow", height=2, width=10)  
b3 = Button(frame, text = "Green", command = lambda : chng_bg_g(b3), activeforeground = "green",activebackground = "yellow", height=2, width=10 )

b1.pack()  
b2.pack()  
b3.pack() 
frame.pack(fill='both', expand=True)

root.mainloop()