def clear_cart(self): #to be added as command in clear btn of billing
    self.var_pid.set("")
    self.var_pname.set("")
    self.var_price.set("")
    self.var_qty.set("")
    self.lbl_inStock.config(text=f"In stock")
    self.var_stock.set("")

def clear_all(self): #to be added as a command in clear all btn
    del self.cart_list[:]
    self.var_cname.set('')
    self.var_contact.set('')
    self.txt_bill_area.delete('1.0',END)
    self.cartTitle.config(text=f"cart \t Total Product:[0]")
    self.var_search.set('')
    self.clear_cart()
    self.show()
    self.show_cart()

#in generate bill function:
    fp=open(f'bill/{str(self.invoice)}.txt','w')
    fp.write(self.txt_bill_area.get('1.0',END))
    fp.close()
    messagebox.showinfo('saved',"bill has been generated and saved in backend",parent=self.root)

#in bill middle function :
     con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
    #put existing code in try block
    try:
       for row in self.cart_list:

        pid=row[0]
        name=row[1]
        qty=int(row[4])-int(row[3])
        if int(qty)==int(row[4]):
           status='Inactive'
        if int(qty)!=int(row[4]):
            status='Active'
            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+qty+"\tRs."+price)
            cur.execute('update product set qty?,status? where pid=?',(
                qty,
                status,
                pid

                ))
        con.commit()
    con.close()
    self.show()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

def update_date_time(self):
    time_=time.strftime("%I:%M:%S")
    date_=time.strftime("%D-%M-%Y")
    self.lbl_clock=config(text="Welcome to Inventory Management System \t\t Date:{str(date_) }\t\t time:{str(time_) }")
    self.lbl.clock.after(200,self.update_date_time)
    #call this function in footer
