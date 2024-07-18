from tkinter import* # tkinter contain the various methods for making GUI
from tkinter import ttk
import sqlite3
class Billing:
    def __init__(self,root): #default method
        self.root=root #the root obj now belongs to class
        self.root.geometry("1350x700+0+0")#geometry is a method which takes height,width,starting,ending pt.
        self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh") #give title to screen
        self.root.config(bg="white")
        #====Title====#
        self.icon_title=PhotoImage(file="images/logo1.png")# can be used only for png images
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("sacramento,cursive",40,"bold"),bg="#30D5C8",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=60)#Label is a part of tkinter class and takes attribute location,text,place defines the location in self.root frame,compound gives location of images

        #====btn__logout=====#
        btn__logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg='yellow',cursor="hand2").place(x=1150,y=10,height=50,width=100) #button function takes various attributes diff is only the cursor attribute

        #=====clock====#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date:DD:MM:YYYY \t\t time:HH:MM:SS",font=("sacramento,cursive",15,),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=60)#placed on 2nd line in the self.root frame

        #==========Product Frame1====#
        self.var_search=StringVar()
        Product_frame1=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Product_frame1.place(x=6,y=110,width=410,height=550)

        ptitle=Label(Product_frame1,text="All Products",font=("times new Roman",15,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #===============product search frame======#
        Product_frame2=Frame(Product_frame1,relief=RIDGE,bd=2,bg="white")
        Product_frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(Product_frame2,text="Search by | Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(Product_frame2,text="product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(Product_frame2,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=128,y=47,height=22,width=150)
        btn_search=Button(Product_frame2,text="search",cursor="hand2",font=("times new roman",15,"bold"),bg="#2196f3",fg="white").place(x=285,y=45,width=100,height=25)
        btn_showAll=Button(Product_frame2,text="show all",cursor="hand2",font=("times new roman",15,"bold"),bg="#083531",fg="white").place(x=285,y=10,width=100,height=25)
        #==============product detail frame======#
        Product_frame3=Frame(Product_frame1,bd=3,relief=RIDGE)
        Product_frame3.place(x=700,y=120,width=395,height=375)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(Product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="Pid")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table["show"]= "heading"     
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)
        #self.cart_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(Product_frame1,text="Note:Enter 0 Qty to remove product from cart",font=("times new roman",12),bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #======Customerframe======#
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        Customerframe=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Customerframe.place(x=420,y=110,width=530,height=70) # previously x was 6+400 width 
        Ctitle=Label(Customerframe,text="Customer Details",font=("times new Roman",15),bg="grey").pack(side=TOP,fill=X)
        lbl_name=Label(Customerframe,text=" Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(Customerframe,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=80,y=35,width=180)
        lbl_contact=Label(Customerframe,text=" Contact No",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(Customerframe,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=380,y=35,width=140)
        #=================Calucator-cart Frame=============================#
        cal_cart_frame=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        cal_cart_frame.place(x=420,y=190,width=530,height=360)
        #============calculator frame
        self.var_cal_input=StringVar()
        cal_frame=Frame(cal_cart_frame,relief=RIDGE,bd=9,bg="white")
        cal_frame.place(x=5,y=10,width=268,height=340)
        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

                #=====cal BUTTON============#
        btn_7=Button(cal_frame,text='7',font=('arial',15,'bold'),bd=5,width=4,command=lambda:self.get_input(7),pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(cal_frame,text='8',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(8),cursor='hand2').grid(row=1,column=1)
        btn_9=Button(cal_frame,text='9',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(9),cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(cal_frame,text='+',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('+'),cursor='hand2').grid(row=1,column=3)


        btn_4=Button(cal_frame,text='4',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(4),cursor='hand2').grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(5),cursor='hand2').grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(6),cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(cal_frame,text='-',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('-'),cursor='hand2').grid(row=2,column=3)

        btn_1=Button(cal_frame,text='1',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(1),cursor='hand2').grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(2),cursor='hand2').grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(3),cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(cal_frame,text='x',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('x'),cursor='hand2').grid(row=3,column=3)

        btn_0=Button(cal_frame,text='0',font=('arial',15,'bold'),bd=5,width=4,pady=15,command=lambda:self.get_input(0),cursor='hand2').grid(row=4,column=0)
        btn_c=Button(cal_frame,text='C',font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2',command=self.perform_cal()).grid(row=4,column=1)
        btn_eq=Button(cal_frame,text='=',font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2',command=self.cal_clear()).grid(row=4,column=2)
        btn_div=Button(cal_frame,text='/',font=('arial',15,'bold'),bd=5,width=4,pady=15,command=lambda:self.get_input('='),cursor='hand2').grid(row=4,column=3)









        #=======================cart-frame=======================#

        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        Cart_title=Label(cart_frame,text="Cart \t total \t product:[0]",font=("times new Roman",15),bg="grey").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)
        self.cart_Table.heading("pid",text="Pid")
        self.cart_Table.heading("name",text="Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("qty",text="QTY")
        self.cart_Table.heading("status",text="Status")
        
        self.cart_Table["show"]= "heading"     
        self.cart_Table.column("pid",width=40)
        self.cart_Table.column("name",width=100)
        self.cart_Table.column("price",width=40)
        self.cart_Table.column("qty",width=50)

        self.cart_Table.column("status",width=90)
        self.cart_Table.pack(fill=BOTH,expand=1)
        #self.cart_Table.bind("<ButtonRelease-1>",self.get_data)
        #============Add cart widgetsFrame================#
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_status=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_cartwidgetsframe=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Add_cartwidgetsframe.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_cartwidgetsframe,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_cartwidgetsframe,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_cartwidgetsframe,text="Price per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_cartwidgetsframe,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(Add_cartwidgetsframe,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_cartwidgetsframe,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=130,height=22)

        self.lbl_p_instock=Label(Add_cartwidgetsframe,text="In stock[9999]",font=("times new roman",15),bg="white")
        self.lbl_p_instock.place(x=5,y=70)

        btn_clear_cart=Button(Add_cartwidgetsframe,text="clear",cursor="hand2",font=("times new roman",15,"bold"),bg="lightgray").place(x=180,y=70,width=150,height=30)
        btn_update_cart=Button(Add_cartwidgetsframe,text="update",cursor="hand2",font=("times new roman",15,"bold"),bg="orange").place(x=340,y=70,width=180,height=30)

        #=================billing area===================#
        billFrame=Frame(self.root,bd=3,releif=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)
        billarea_title=Label(billFrame,text="Customer bill area",font=("times new Roman",15),bg="#2626F").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,font=('goudy old stylr',28,'bold'),yscrollcommand=scrolly)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        #===================bill Buttons=============#
        bill_menu_Frame=Frame(self.root,bd=2,releif=RIDGE,bg="white")
        bill_menu_Frame.place(x=953,y=520,width=410,height= 140)
        self.lbl_amt=Label(bill_menu_Frame,text='bill amount \n [0]',font=("goudy old style",15,"bold"),bg="#3f51b5")
        self.lbl_amt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(bill_menu_Frame,text='discount \n 5%',font=("goudy old style",15,"bold"),bg="#8bc34a")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netpay=Label(bill_menu_Frame,text='Net Pay \n [0]',font=("goudy old style",15,"bold"),bg="#607d8bs")
        self.lbl_netpay.place(x=246,y=5,width=120,height=70)

        btn_print=Button(bill_menu_Frame,text='print bill',cursor="hand2",font=("goudy old style",15,"bold"),bg="red")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear=Button(bill_menu_Frame,text='clear bill',cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen")
        btn_clear.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(bill_menu_Frame,cursor="hand2",text='generate bill',font=("goudy old style",15,"bold"),bg="purple")
        btn_generate.place(x=246,y=80,width=120,height=50)

        #===================footer========================#
        self.show()
        

















        #=========================ALL FUNCTIONS======================#

        def get_input(self,num):
            xnum=self.var_cal_input.get()+str(num)
            self.var_cal_input.set(xnum)
        def cal_clear(self):
            self.var_cal_input.set(" ")
        def perform_cal(self):
            result=self.var_cal_input.get()
            self.var_cal_input.set(eval(result))
        
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            #self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","Name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select pid,Name,price,qty,status from product")
            rows=cur.fetchall()
            self.product_Table.delete(self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
                Message.showerror("error",f"error due to:{str(ex)}",parent=self.root)





        
if __name__=="___main__":
    root=Tk() #tk class belongs to tkinter module
    obj=Billing(root)
    root.mainloop() #used to keep the window stable