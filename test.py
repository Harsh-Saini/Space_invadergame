from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Calculator")
        self.pack(fill=BOTH, expand= 1)
        #quitbutton= Button(self, text= 'Quit', command= self.exit_button)
        #quitbutton.place(x=0,y=0)

        my_menu = Menu(self.master, tearoff=0)
        self.master.config(menu=my_menu)

        file = Menu(my_menu)
        file.add_command(label='Exit', command=self.exit_button())
        my_menu.add_cascade(label='File', my_menu=file)

    def exit_button(self):
        exit()
        


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
