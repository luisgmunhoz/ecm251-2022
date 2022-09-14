from tkinter import *
from tkinter import font

root = Tk()
root.title("Fonts")
root.geometry("600x600")

def select_font(e):
    selected_font.config(family = listbox.get(listbox.curselection()))
selected_font = font.Font(family = "Helvetica",size = "32")
frame = Frame(root,width=480,height=275)
frame.pack(pady = 10)

frame.grid_propagate(False)
frame.columnconfigure(0,weight=10)

text = Text(frame,font=selected_font)
text.grid(row=0,column=0)
text.grid_rowconfigure(0,weight=1)
text.grid_columnconfigure(0,weight=1)

listbox = Listbox(root,selectmode = SINGLE,width=80)
listbox.pack()

for i in font.families():
    listbox.insert('end',i)

listbox.bind('<ButtonRelease-1>',select_font)
root.mainloop()
