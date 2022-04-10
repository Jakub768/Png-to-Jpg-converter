import tkinter as tk
from tkinter import filedialog
from PIL import Image

Window = tk.Tk()
Window.resizable(False, False)
Window.title("PNGtoJPG")

class app():

    def __init__(self, parent):
        self.createWidgets(parent)
    
    def createWidgets(self, main):
        mainFrame = tk.Frame(main)

        #Labels
        self.Heading = tk.Label(mainFrame, text="Welcome to the \n PNG to JPG converter!", font="Bold", pady=10).grid(row=0, column=1)

        #Buttons
        self.Convert = tk.Button(mainFrame, text="Convert to JPG", pady=5, command=self.convert).grid(row=1, column=2)
        self.importJPGButton = tk.Button(mainFrame, text="Import a PNG image", pady=5, command=self.getImage).grid(row=1, column=0)

        self.list = tk.Listbox(mainFrame, height=5).grid(row=1,column=1)

        mainFrame.pack()

    def getImage(self):
        global image_temp

        self.filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        image_temp = Image.open(self.filename)


    def convert(self):
        global image_temp

        rgb_im = image_temp.convert('RGB')
        exporttojpg = filedialog.asksaveasfilename(defaultextension='.jpg')
        rgb_im.save(exporttojpg)

p = app(Window)
Window.mainloop()
        
