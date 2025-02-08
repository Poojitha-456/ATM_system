import sqlite3 as sql
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def display_image():
    try:
        conn = sql.connect('ATMdata.db')
        cursor = conn.execute("SELECT IMAGE FROM IMAGES WHERE ID=?", (e1.get(),))
        img_data = cursor.fetchone()
        conn.close()
        if img_data:
            with open('test.png', 'wb') as file:
                file.write(img_data[0])
                img = ImageTk.PhotoImage(Image.open('test.png'))
                panel.configure(image=img)
                panel.image = img
        else:
            # If no image found for the provided ID, display a placeholder or handle accordingly
            print("No image found for the provided ID.")
    except Exception as e:
        print("Error:", e)

win = tk.Tk()
win.geometry("700x500")

l3 = tk.Label(win, text='ID', font=("Arial", 15), bg='#E1AFD1')
l3.pack()

e1 = tk.Entry(win, show=None, font=('Arial', 15), bg='#E1AFD1')
e1.pack()

img = ImageTk.PhotoImage(Image.open("White_full.jpg"))
panel = tk.Label(win, image=img)
panel.image = img
panel.pack()

subtn = tk.Button(win, text="SUBMIT", width=20, height=2, command=display_image)
subtn.pack()  # This line was previously missed

win.mainloop()
