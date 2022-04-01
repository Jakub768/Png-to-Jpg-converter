from tkinter import *


Window = Tk()
Window.resizable(False, False)
Window.title("PNGtoJPG")

class app():

    def __init__(self, parent):
        self.createWidgets(parent)
    
    def createWidgets(self, main):
        mainFrame = Frame(main)

        self.importJPGButton = Button(mainFrame, text="Import a JPG image", pady=5, command=self.getImage).grid(row=1, column=0)
        self.Convert = Button(mainFrame, text="Convert to PNG", pady=5, command=self.getImage).grid(row=1, column=1)

        mainFrame.pack()

    def getImage(self):
        pass

    def convert(self):
        pass

p = app(Window)
Window.mainloop()
        
