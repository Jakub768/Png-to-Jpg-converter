from tkinter import * 

Window = Tk()
Window.title("PNGtoJPG")
Window.geometry("200x200")

class app():

    def __init__(self, parent):
        self.createWidgets(parent)
    
    def createWidgets(self, main):
        mainFrame = Frame(main)

        self.importJPGButton = Button(mainFrame, text="Import a PNG image", pady=20, command=self.getImage).grid(row=0, column=0)

        mainFrame.pack()

    def getImage(self):
        pass

    def convert(self):
        pass

p = app(Window)
Window.mainloop()
        
