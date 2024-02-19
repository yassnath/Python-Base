from tkinter import *

window = Tk()
window.title("HelloGUI")
window.geometry("300x100")
l = Label(window, text = "Hello!")
l.pack()
b = Button(window, text = "Click me")
b.pack()
window.mainloop()