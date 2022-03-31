from tkinter import *

Window = Tk()
Window.title("PNGtoJPG")
Window.geometry("600x600") 

class app():

    def __init__(self, parent):
        self.objects(parent)
    
    def objects(self, main):
        mainFrame = Frame(main)
        mainFrame.grid(column=0, row=0)

        self.importJPGButton = Button(main, text="Import a JPG image", command=self.getinfo)
        self.importJPGButton.grid(column=1,row=1)

    def getinfo(self):
        print("the program works")
    
p = app(Window)
Window.mainloop()
        
