from tkinter import *
def hi():
    print("Hi!")

window = Tk()
window.title("HelloGUI")
window.geometry("300x100")
l = Label(window, text = "Hello!")
l.pack()
b = Button(window, text = "Click me", command = hi)
b.pack()
window.mainloop()