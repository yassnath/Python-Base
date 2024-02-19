import tkinter
 
master=tkinter.Tk() 
master.title("pack() method") 
master.geometry("450x350")

button1=tkinter.Button(master, text="LEFT") 
button1.pack(side=tkinter.LEFT)

button2=tkinter.Button(master, text="RIGHT") 
button2.pack(side=tkinter.RIGHT)

button3=tkinter.Button(master, text="TOP") 
button3.pack(side=tkinter.TOP)

button4=tkinter.Button(master, text="BOTTOM") 
button4.pack(side=tkinter.BOTTOM)

master.mainloop()