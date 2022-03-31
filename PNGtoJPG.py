from tkinter import * 

Window = Tk()
Window.title("PNGtoJPG")
Window.geometry("200x200")

class app():

    def __init__(self, main):
        mainFrame = Frame(main)

        self.importJPGButton2 = Button(mainFrame, text="Import a PNG image", pady=20, command=self.getinfo).grid(row=0, column=0)

        mainFrame.pack()

    def getImage(self):
        print("the program works")

    def convert(self):
        pass

p = app(Window)
Window.mainloop()
        
