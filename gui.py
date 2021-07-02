#Imports tkinter
from tkinter import *
import tkinter
import notify2
notify2.init(app_name="tkinter Clicker")
n = notify2.Notification("Whoosh! Notifications are a go!","'Click'","notification-message-im",)

#Makes class for Window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Menu Creation
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        # Label Creation

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.exitProgram)
        exitButton.pack()
        #exitButton.place(x=268, y=170)
        clickButton = Button(self, text="Send NotifIcations", width=25,height=5,bg="blue",fg="yellow",command= n.show)
        clickButton.place(x=0,y=0)
        #clickButton.pack()
        textEntry = Entry(self,text="hello",fg="black", bg="green", width=10)
        textEntry.pack()
    def exitProgram(self):
        exit()



root = Tk()
app = Window(root)
root.wm_title("Not a game")
root.geometry("600x300")
root.mainloop()
