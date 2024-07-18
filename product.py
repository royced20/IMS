from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="White")
        self.root.focus_force()
        #=============================================
        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_pid=StringVar()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #=========title========================
        title = Label(product_Frame,text = "Manage Product Details",font =("Goudy old style",18), bg = "#0f4d7d",fg="white").pack(side=TOP,fill=X)
         
         #======column1========
        lbl_category= Label(product_Frame,text = "Category",font =("Goudy old style",18),bg="white").place(x=30,y=60)
        lbl_sup= Label(product_Frame,text = "Supplier",font =("Goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name= Label(product_Frame,text = "Name",font =("Goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price= Label(product_Frame,text = "Price",font =("Goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty= Label(product_Frame,text = "Quantity",font =("Goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status= Label(product_Frame,text = "Status",font =("Goudy old style",18),bg="white").place(x=30,y=310)
        
        
         #--------column2--------
        cmb_cat = ttk.Combobox(product_Frame,textvariable = self.var_cat,values =self.cat_list,state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)


        cmb_sup = ttk.Combobox(product_Frame,textvariable = self.var_sup,values = self.sup_list,state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable = self.var_name,font = ("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable = self.var_price,font = ("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable = self.var_qty,font = ("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)

        cmb_status= ttk.Combobox(product_Frame,textvariable = self.var_status,values = ("Active","Inactive"),state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

 #=====================button======
        btn_add = Button(product_Frame,text = "Save",command = self.add,font =("Goudy old style",15), bg = "#2196f3",cursor = "hand2").place(x = 10,y =400,width = 100,height = 40)
        btn_update = Button(product_Frame,text = "Update",command = self.update,font =("Goudy old style",15), bg = "#4caf50",cursor = "hand2").place(x = 120,y =400,width = 100,height = 40)
        btn_delete = Button(product_Frame,text = "Delete",command = self.delete,font =("Goudy old style",15), bg = "#f44336",cursor = "hand2").place(x = 230,y =400,width = 100,height = 40)
        btn_clear = Button(product_Frame,text = "Clear",command = self.clear,font =("Goudy old style",15), bg = "#607d8b",cursor = "hand2").place(x = 340,y =400,width = 100,height = 40)

         #----------Search Frame------------

        Search_Frame = LabelFrame(self.root,text = "Search Products",font = ("goudy old style",12,"bold"),bg = "white", bd =2,relief = RIDGE)
        Search_Frame.place(x = 480,y = 10,width = 600,height = 80 )

        #--------option--------

        cmb_Search = ttk.Combobox(Search_Frame,textvariable = self.var_searchby,values = ("Search","Category","Supplier","Name"),state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_Search.place(x = 10, y= 10, width = 180)
        cmb_Search.current(0)

        text_search = Entry(Search_Frame,textvariable = self.var_searchtext,font =("Goudy old style",15), bg = "Light yellow").place(x = 200,y = 10,width = 260,height =30)
        btn_search = Button(Search_Frame,text = "Search",command = self.search,font =("Goudy old style",15), bg = "Green",cursor = "hand2").place(x = 470,y = 5,width = 120,height = 35)


        #-----------product details-----------

        p_frame = Frame(self.root, bd = 3,relief = RIDGE)
        p_frame.place(x =480,y =100,width =600,height = 390) 

        scrolly = Scrollbar(p_frame,orient = VERTICAL)
        scrollx = Scrollbar(p_frame,orient = HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame,columns= ("pid","Supplier","Category","name","price","qty","status"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set )
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.product_table.xview)
        scrolly.config(command = self.product_table.yview)

       
        self.product_table.heading("pid",text = "P ID")
        self.product_table.heading("Category",text = "Category")
        self.product_table.heading("Supplier",text = "Supplier")
        self.product_table.heading("name",text = "Name")
        self.product_table.heading("price",text = "Price")
        self.product_table.heading("qty",text = "Qty")
        self.product_table.heading("status",text = "Status")
       
        self.product_table["show"] = "headings"
        self.product_table.pack(fill = BOTH,expand = 1)


        self.product_table.column("pid",width = 90)
        self.product_table.column("Category",width = 100)
        self.product_table.column("Supplier",width = 100)
        self.product_table.column("name",width = 100)
        self.product_table.column("price",width = 100)
        self.product_table.column("qty",width = 100)
        self.product_table.column("status",width = 100)
        
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
       
#--------------------Add Function------------------------------------
     
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


    def add(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty"  or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are  be required",parent = self.root)
            else:
                cur.execute("Select *from employee where name=?",(self.var_name.get(),))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error","Product is already present",parent = self.root )
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                       
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","Product added Succesfully",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Show Function------------------------------------

    def show(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
         cur.execute("Select * from product")
         rows = cur.fetchall() 

         self.product_table.delete(*self.product_table.get_children())

         for row in rows:
             self.product_table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Get Data Function------------------------------------

    def get_data(self,ev):

        f = self.product_table.focus()
        content = (self.product_table.item(f)) 
        row = content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_supplier.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])                
                       
       
#--------------------Update Function------------------------------------

    def update(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error","Select product from list",parent = self.root)
            else:
                cur.execute("Select *from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root )
                else:
                    cur.execute("UPDATE product set Category=?,Supplier=?,name=?,price=?,qty=?,status=?, WHERE pid =? ;",(
                        self.var_cat.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Succesfully",parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Delete Function------------------------------------

    def delete(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error","Select product from list",parent = self.root)
            else:
                cur.execute("Select *from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Product",parent = self.root )
                else:
                    op = messagebox.askyesno("Confirm","Are you realy want to delete?",parent = self.root)
                    if op == True:
                        cur.execute("Delete from product where pid = ?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Succesfully",parent = self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)            


#--------------------Clear Function------------------------------------

    def clear(self):

       self.var_cat.set("Select"),
       self.var_supplier.set("Select"),
       self.var_name.set(""),
       self.var_price.set(""),
       self.var_qty.set(""),
       self.var_status.set("Active"),           
       self.var_pid.set("") 

       self.var_searchby.set("Select")
       self.var_searchtext.set("")
       self.show()


#--------------------Search Function------------------------------------

    def search(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_searchby.get()=="Select":
              messagebox.showerror("Error","Select Search by Option",parent = self.root)

            elif self.var_searchtext.get()=="":
              messagebox.showerror("Error","Search input required",parent = self.root)
            
            else:
              cur.execute("Select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
              rows = cur.fetchall() 

              if len(rows)!=0:
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                    self.product_table.insert('',END,values = row)
              else:
                  messagebox.showinfo("Error","No record found",parent = self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


if __name__=="__main__":
    root=Tk()
    obj=productClass(root    )
    root.mainloop()
    