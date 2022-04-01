import tkinter as tk
from tkinter import filedialog


Window = tk.Tk()
Window.resizable(False, False)
Window.title("PNGtoJPG")

class app():

    def __init__(self, parent):
        self.createWidgets(parent)
    
    def createWidgets(self, main):
        mainFrame = tk.Frame(main)

        self.Heading = tk.Label(mainFrame, text="Welcome to the \n PNG to JPG converter!", font="Bold", pady=10).grid(row=0, column=1)
        self.Convert = tk.Button(mainFrame, text="Convert to JPG", pady=5).grid(row=1, column=2)
        self.importJPGButton = tk.Button(mainFrame, text="Import a PNG image", pady=5, command=self.getImage).grid(row=1, column=0)

        self.list = tk.Listbox(mainFrame).grid(row=1,column=1)

        mainFrame.pack()

    def getImage(self):
        self.filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))

    def convert(self):
        pass

p = app(Window)
Window.mainloop()
        
