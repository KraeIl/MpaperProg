from tkinter import *
import time

class MenuPrincipal:
    def __init__(self, cesar):
        self.master = cesar
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')

        cesar.title("A simple GUI")

        self.label = Label(cesar, text=self.time2, font= ('times', 12, 'bold'))
        self.label.after(cesar, 200, 'tick')
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.greet_button = Button(cesar, text="Greet", command=self.greet)
        self.greet_button.place(relx=0.0, rely=1.0, anchor='sw')

        self.close_button = Button(cesar, text="Close", command=cesar.quit)
        self.close_button.place(relx=1.0, rely=1.0, anchor='se')

    def greet(self):
        print("Greetings!")



root = Tk()
root.attributes('-fullscreen', 1)
my_gui = MenuPrincipal(root)
root.mainloop()
