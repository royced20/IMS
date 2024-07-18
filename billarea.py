
from tkinter import* # tkinter contain the various methods for making GUI
from tkinter import ttk
class Billing:
    def __init__(self,root): #default method
        self.root=root #the
        root obj now belongs to class
        #self.root.geometry("1350x700+0+0")#geometry is a method which takes height,width,starting,ending pt.
        #self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh") 
if __name__=="___main__":
    root=Tk() #tk class belongs to tkinter module
    obj=Billing(root)
    root.mainloop() #used to keep the window stable