print("hello world")
print("my name is royce")
from tkinter import* # tkinter contain the various methods for making GUI
from PIL import Image,ImageTk
from employee import employee_class
from sales import salesClass
class IMS:
    def __init__(self,root): #default method
        self.root=root #the root obj now belongs to class
        self.root.geometry("1350x700+0+0")#geometry is a method which takes height,width,starting,ending pt.
        self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh") #give title to screen
        #====Title====#
        self.icon_title=PhotoImage(file="images/logo1.png")# can be used only for png images
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("sacramento,cursive",40,"bold"),bg="#30D5C8",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=60)#Label is a part of tkinter class and takes attribute location,text,place defines the location in self.root frame,compound gives location of images

        #====btn__logout=====#
        btn__logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg='yellow',cursor="hand2").place(x=1150,y=10,height=50,width=100) #button function takes various attributes diff is only the cursor attribute

        #=====clock====#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date:DD:MM:YYYY \t\t time:HH:MM:SS",font=("sacramento,cursive",15,),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=60)#placed on 2nd line in the self.root frame
        #====leftMenu===#
        self.Menulogo=Image.open("images/menu_im.png") #open the image with Image.open("path")
        self.Menulogo=self.Menulogo.resize((200,200),Image.ANTIALIAS) #resize the image as its too big and Antialias doesnt alter the clarity
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo) #we again open the image without specifying the path using imagetk class of PIL module

        leftMenu=Frame(self.root,bd=2,relief=RIDGE) # frame is created in self.root,with border 2px,ridge border
        leftMenu.place(x=0,y=200,height=500,width=200) # It is placed at mentioned location

        lbl_menulogo=Label(leftMenu,image=self.Menulogo) # label is added with the image
        lbl_menulogo.pack(side=TOP,fill=X) #fill=X denotes that it would the frame area available in x direction
        lbl_menu=Label(leftMenu,text="Menu",font=("sacramento,cursive",15,"bold"),bg="Green").pack(side=TOP,fill=X)# used for menu label


        self.icon_side=PhotoImage(file="images/side.png")
        btn_employee=Button(leftMenu,text="Employee",image=self.icon_side,compound=LEFT,command=self.employee,padx=20,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X)# employee button
        btn_supplier=Button(leftMenu,text="supplier",image=self.icon_side,compound=LEFT,padx=20,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X)# supplier button
        btn_category=Button(leftMenu,text="category",image=self.icon_side,compound=LEFT,padx=20,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X)# category button
        btn_product=Button(leftMenu,text="product",image=self.icon_side,compound=LEFT,padx=20,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X) #product button
        btn_sales=Button(leftMenu,text="sales",image=self.icon_side,compound=LEFT,padx=20,command=self.sales,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X) #sales button
        btn_exit=Button(leftMenu,text="exit",image=self.icon_side,compound=LEFT,padx=20,font=("sacramento,cursive",15,"bold"),bg="white",cursor="hand2",anchor=W).pack(side=TOP,fill=X) # exit button
        
        #=====Content========================#
       
        self.lbl_employee=Label(self.root,text="Total Employee \n [0]",bg="#33bbf9",fg="white",bd=5,relief=RAISED,font=("san-serif",20,"bold"))
        self.lbl_employee.place(x=300,y=170,height=150,width=300) # employee label

        self.lbl_supplier=Label(self.root,text="Total Supplier \n [0]",bg="#33be79",fg="white",bd=5,relief=RAISED,font=("san-serif",20,"bold"))
        self.lbl_supplier.place(x=650,y=170,height=150,width=300) # supplier label
        
        self.lbl_category=Label(self.root,text="Total Category \n [0]",bg="#009688",fg="white",bd=5,relief=RAISED,font=("san-serif",20,"bold"))
        self.lbl_category.place(x=1000,y=170,height=150,width=300) # category label
        
        self.lbl_product=Label(self.root,text="Total product \n [0]",bg="#607d8b",fg="white",bd=5,relief=RAISED,font=("san-serif",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300) # product label
       
        self.lbl_sales=Label(self.root,text="Total sales \n [0]",bg="#ffc107",fg="white",bd=5,relief=RAISED,font=("san-serif",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300) # sales label
        

        
        
        #===footer====#
        self.lbl_footer=Label(self.root,text="IMS-Inventory Management System |\n Contact \t Jatin \t Royce\t Darsh",font=("sacramento,cursive",15,),bg="black",fg="white").pack(side=BOTTOM,fill=X)# adding footer
#==================================================================================================#
    def employee(self): # called in the employee button
        self.new_win=Toplevel(self.root)
        self.new_obj=employee_class(self.new_win) #object belongs to employee_class of employee file and the function is called in employee button
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)


if __name__=="___main__":
    root=Tk() #tk class belongs to tkinter module
    obj=IMS(root)
    root.mainloop() #used to keep the window stable