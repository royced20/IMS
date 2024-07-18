from tkinter import* # tkinter contain the various methods for making GUI
from PIL import Image,ImageTk
class employee_class:
    def __init__(self,root): #default method
        self.root=root #the root obj now belongs to class
        self.root.geometry("1100x500+220+130")#geometry is a method which takes height,width,starting,ending pt.
        self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh") #give title to screen
        if __name__=="___main__":

            root=Tk() #tk class belongs to tkinter module
            obj=employee_class(root)
            root.mainloop() #used to keep the window stable