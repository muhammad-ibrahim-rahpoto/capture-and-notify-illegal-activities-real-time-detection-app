import os
from tkinter import *;
from tkinter import messagebox

root = Tk()
root.title("DASHBORAD")
width, height = 1400,700
root.geometry(f"{width}x{height}")
root.configure(bg='#FFF')
root.resizable(True, True)

def button1_click():
    specific_folder_path = "F:\DETECTED PERSON"  # Replace with your desired folder path
    os.startfile(specific_folder_path)


def button2_click():
    os.system("main.py")
    root.destroy()


# Create circular button 1
button1_img = PhotoImage(file=r"C:\Users\Muhammad Ibrahim\Desktop\1.jpg")

button1 = Button(root, image=button1_img, command=button1_click, bd=0)
button1.pack(side=TOP, padx=10, pady=20)

# Create circular button 2
button2_img = PhotoImage(file=r"C:\Users\Muhammad Ibrahim\Desktop\1.jpg")

button2 = Button(root, image=button2_img, command=button2_click, bd=0)
button2.pack(side=BOTTOM, padx=10, pady=20)


# Start the tkinter event loop
root.mainloop()