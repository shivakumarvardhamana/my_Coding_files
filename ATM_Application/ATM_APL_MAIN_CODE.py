# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:12:46 2022

@author: vardh
"""


import mysql.connector

"""mydb=mysql.connector.connect(host="localhost",user="chary",passwd="1234",database="shiva")

mycurson=mydb.cursor()

mycurson.execute("select name,salary from student2 where id =1234")

for i in mycurson:
    print(i)"""
    
    
    
    
# -*- coding: utf-8 -*-
#Created on Sun May 15 21:44:58 2022

#@author: vardh



from tkinter import *



class atm:
    
    def __init__(self,win):
        self.temp="1"
        self.pin=1234
        self.Amount=10000
        self.name="shiva kumar vardhaman"
        self.Ac_num=12345
        self.Branch="Hyderabad"
        self.AC_type="Savings"
        self.Adress="Upaal,Hyderabad"
        

        self.mydb=mysql.connector.connect(host="localhost",user="chary",passwd="1234",database="shiva")

        self.mycurson=self.mydb.cursor()
        """self.mycurson3=self.mydb.cursor()
        self.mycurson3.execute("select * from s1")
        self.n=self.mycurson3.fetchall()
        for i in self.n:
            print(i)"""
        

        
        
        
        
                
            
        
        


        
        
        self.std=Button(win,text="balanece",bg="light blue",command=self.balance)
        self.std.place(x=20,y=20)
        self.std.bind("<Enter>",self.entered)
        self.std.bind("<Leave>",self.left)
        #myd=self.mydb.cursor()
        
        #self.std.bind('<Button-1>', self.hide_me)
        self.std4=Button(win,text="AC_Detail",bg="light blue",command=self.checkpin)
        self.std4.place(x=20,y=280)
    

        self.std4.bind("<Enter>",self.entered1)
        self.std4.bind("<Leave>",self.left1)
    

        self.std2=Button(win,text="withdraw",bg="light blue",command=self.withdraw)
        self.std2.place(x=20,y=100)
        self.std2.bind("<Enter>",self.entered2)
        self.std2.bind("<Leave>",self.left2)
        self.std2.bind('<Button-1>', self.hide_me1)
        
        self.std3=Button(win,text="Deposit",bg="light blue",command=self.deposit)
        
        self.std3.place(x=20,y=200)
        self.std3.bind("<Enter>",self.entered3)
        self.std3.bind("<Leave>",self.left3)
        self.std3.bind('<Button-1>', self.hide_me2)
    def Alert(self):
        self.te7=Label(win,text="PIN_Number is Incorrect",font=('bolt 25'))
        self.te7.place(x=200,y=180)
    def checkpin(self):

        self.std2.bind("<Button-1>")
        self.std2.place_forget()
        self.std3.bind("<Button-1>")
        self.std3.place_forget()
        self.std2.bind("<Button-1>")
        self.std2.place_forget()
        self.std.bind("<Button-1>")
        self.std.place_forget()
        self.std2.bind("<Button-1>")
        self.std2.place_forget()
        self.std4.bind("<Button-1>")
        self.std4.place_forget()
        self.te5=Label(win,text="Enterpin",font=('Calibri 10'))
        self.te5.place(x=300,y=100)
        


        self.a5=Entry(win,width=25)
        self.a5.place(x=350,y=100)
        
        self.btn5=Button(win,text="checking",command=self.acdetail)
        self.btn5.place(x=380,y=120)
    
    def acdetail(self):

        self.t5=int(self.a5.get())
        self.te5.bind("<Button-1>")
        self.te5.place_forget()
        self.a5.bind("<Button-1>")
        self.a5.place_forget()
        self.btn5.bind("<Button-1>")
        self.btn5.place_forget()
        self.mycurson2=self.mydb.cursor()
        self.mycurson2.execute("select salary from s1 where id=%s and temp=%s",(self.a5.get(),self.temp))
        self.row11=self.mycurson2.fetchone()
        

        #self.row12=(str(self.row1))
        #self.row3=int(self.row2)
        if self.row11 != None:
            self.my10=self.mydb.cursor()
            self.my10.execute("select name from s1 where id=%s and temp=%s",(self.a5.get(),self.temp))
            self.row15=self.my10.fetchone()
            print(self.row15)
            self.s13=""
            for i in self.row15:
                if i=='(' or  i==')' or i==',':
                    continue
                else:
                    self.s13=self.s13+i
            self.my11=self.mydb.cursor()
            self.my11.execute("select id from s1 where id=%s and temp=%s",(self.a5.get(),self.temp))
            self.row16=self.my11.fetchone()
            print(self.row16)
            self.row17=str(self.row16)
            self.s14=""
            for i in self.row17:
                if i=='(' or  i==')' or i==',':
                    continue
                else:
                    self.s14=self.s14+i
            self.s15=str(self.Ac_num)+self.s14
            self.s16=int(self.s15)
            self.te6=Label(win,text="Account_Holder_Deatails",font=('bolt 25'))
            self.te6.place(x=200,y=40)
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std3.bind("<Button-1>")
            self.std3.place_forget()
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std.bind("<Button-1>")
            self.std.place_forget()
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std4.bind("<Button-1>")
            self.std4.place_forget()
            self.lab=Label(win,text="Name:",font=('Calibri 15'))
            self.lab.place(x=200,y=100)
            self.lab2=Label(win,text="Name",font=('Calibri 15'))
            self.lab2.place(x=280,y=100)
            self.lab2.config(text=self.s13)
            self.lab3=Label(win,text="AC_number:",font=('Calibri 15'))
            self.lab3.place(x=150,y=140)
            self.lab4=Label(win,text="A_num",font=('Calibri 15'))
            self.lab4.place(x=280,y=140)
            self.lab4.config(text=self.s16)
            self.lab5=Label(win,text="Branch:",font=('Calibri 15'))
            self.lab5.place(x=190,y=180)
            self.lab6=Label(win,text="Branch",font=('Calibri 15'))
            self.lab6.place(x=280,y=180)
            self.lab6.config(text=self.Branch)
            self.lab7=Label(win,text="AC_type:",font=('Calibri 15'))
            self.lab7.place(x=180,y=220)
            self.lab8=Label(win,text="AC_type",font=('Calibri 15'))
            self.lab8.place(x=280,y=220)
            self.lab8.config(text=self.AC_type)
            #self.lab9=Label(win,text="Adress:",font=('Calibri 15'))
            #self.lab9.place(x=190,y=260)
            #self.lab10=Label(win,text="Adress:",font=('Calibri 15'))
            #self.lab10.place(x=280,y=260)
            #self.lab10.config(text=self.Adress)
        else:
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std3.bind("<Button-1>")
            self.std3.place_forget()
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std.bind("<Button-1>")
            self.std.place_forget()
            self.std2.bind("<Button-1>")
            self.std2.place_forget()
            self.std4.bind("<Button-1>")
            self.std4.place_forget()
            self.Alert()
    def balance(self):
        
        

       self.std4.bind("<Button-1>")
       self.std4.place_forget()
       self.std2.bind("<Button-1>")
       self.std2.place_forget()
       self.std3.bind("<Button-1>")
       self.std3.place_forget()
       #self.std['state']='disable
       self.std.bind("<Button-1>")
       self.std.place_forget()   
       self.te=Label(win,text="Enterpin",font=('Calibri 10'))
       self.te.place(x=300,y=100)
       
       self.a=Entry(win,width=25)
       self.a.place(x=350,y=100)
       #self.a.config({"background": "light blue"})
       self.btn=Button(win,text="checking",command=self.enquiry)
       self.btn.place(x=380,y=120)
       

       #self.te1=Label(win,text="Entersal",font=('Calibri 10'))
       #self.te1.place(x=300,y=140)
        
       #self.a6=Entry(win,width=25)
       #self.a6.place(x=350,y=140)


       #self.te1=Label(win,text="EnterAm",font=('Calibri 10'))
       #self.te1.place(x=300,y=140)
       #self.a8=Entry(win,width=25)
       #self.a8.place(x=350,y=140)


        


        
   
        
        
    #def deposit(self):
        #print("I am fromo deposit")
    def enquiry(self):
        self.te.bind("<Button-1>")
        self.te.place_forget()
        self.a.bind("<Button-1>")
        self.a.place_forget()
        self.btn.bind("<Button-1>")
        self.btn.place_forget()
        #self.t=int(self.a.get())
        #self.let=list(self.a.get())
        #sal=list(1000)
        #n=(1000,)
        my5=self.mydb.cursor()
        my3=self.mydb.cursor()
        my4=self.mydb.cursor()
        my3.execute("select salary from s1 where id=%s and temp=%s",(self.a.get(),self.temp))
        re=my3.fetchone()
        re1=str(re)
        if re!= None:
            
        
            s10=""
            for i in re1:
                if i=='(' or  i==')' or i==',':
                    continue
                else:
                    s10=s10+i
        
            re2=int(s10)
            print(re2)
            self.la=Label(win,text="Balance:",font=('Calibri 15'))
            self.la.place(x=250,y=180)
            label=Label(win, text="Balance: ", font=('Calibri 15'))
            label.place(x=350,y=180)
            label.config(text=re2)
        else:
            self.Alert()
        """re3=int(self.a8.get())
        val=re2+re3
        val1=str(val)
        print(val)
        my4.execute("update s1 set salary=%s where id=%s",(val1,self.a.get()))
        self.mydb.commit()
        my5.execute("select salary s1")
        #ro5=my5.fetchone()
        for i in my5:
            print(i)
        #print(r2)
         
        #my3.execute("update student4 set salary=salary+n where id=%s and temp=%s",(self.a8.get(),self.a.get(),self.temp))
        
        #my4.execute("select salary from studet4 where id=%s and temp=%s",(self.a.get(),self.temp))
        
        #reo=my4.fetchone()
        #print(reo)
        self.mycurson.execute("select salary from s1 where id=%s and temp=%s",(self.a.get(),self.temp))
        row=self.mycurson.fetchone()
        row1=(str(row))
        #print(row1)
        s10=""
        for i in row1:
            if i=='(' or  i==')':
                continue
            else:
                s10=s10+i
                
        print(s10)
        self.la10=Label(win,text="Balance:",font=('Calibri 15'))
        self.la10.place(x=250,y=180)
        label1=Label(win, text="Balance: ", font=('Calibri 15'))
        label1.place(x=350,y=180)
        label1.config(text=s10)
        #print(s)
        #for self.i in self.mycurson:"""
            
           
            
            

    def hide_me(self, event):
        
        print('hide me')
        event.widget.place_forget()
        self.balance()
        
    def withdraw(self):
        self.std4.bind("<Button-1>")
        self.std4.place_forget()
        self.std.bind("<Button-1>")
        self.std.place_forget()
        self.std3.bind("<Button-1>")
        self.std3.place_forget()
        self.te1=Label(win,text="Enter",font=('Calibri 10'))
        self.te1.place(x=300,y=100)
        self.a3=Entry(win,width=25)
        self.a3.place(x=350,y=100)
        self.btn1=Button(win,text="continue",command=self.enquiry1)
        self.btn1.place(x=380,y=120)
        
    def enquiry1(self):
        self.te1.bind("<Button-1>")
        self.te1.place_forget()
        #self.mycurson=self.mydb.curson()
        self.mycurson.execute("select salary from s1 where id=%s and temp=%s",(self.a3.get(),self.temp))
        self.row1=self.mycurson.fetchone()
        self.row2=(str(self.row1))
        #self.row3=int(self.row2)
        #print(row1)

        if self.row1 != None:
            
            self.a3.bind("<Button-1>")
            self.a3.place_forget()
            self.btn1.bind("<Button-1>")
            self.btn1.place_forget()
            self.la1=Label(win,text="EnterAMOUNT",font=('Calibri 15'))
            self.la1.place(x=220,y=95)
            self.b=Entry(win,width=35)
            self.b.place(x=350,y=100)
            self.Btn2=Button(win,text="proceed",command=self.final)
            self.Btn2.place(x=380,y=120)
            #label1=Label(win, text="Balance: ", font=('Calibri 15'))
            ##label1.place(x=100,y=80)
            #@label1.config(text=self.Amount)
            #print("Balance Amount:",self.Amount)
            #Label(win,text="yes",font=('Calibri 10')).pack()
        else:
            self.a3.bind("<Button-1>")
            self.a3.place_forget()
            self.btn1.bind("<Button-1>")
            self.btn1.place_forget()
            self.Alert()
    def deposit(self):
        self.std4.bind("<Button-1>")
        self.std4.place_forget()
        self.std.bind("<Button-1>")
        self.std.place_forget()
        self.std2.bind("<Button-1>")
        self.std2.place_forget()
        self.te3=Label(win,text="EnterP",font=('Calibri 10'))
        self.te3.place(x=300,y=100)
        self.a3=Entry(win,width=25)
        self.a3.place(x=350,y=100)
        self.btn3=Button(win,text="continue",command=self.enquiry2)
        self.btn3.place(x=380,y=120)
            
    def enquiry2(self):
        self.te3.bind("<Button-1>")
        self.te3.place_forget()
        self.mycurson1=self.mydb.cursor()
        self.mycurson1.execute("select salary from s1 where id=%s and temp=%s",(self.a3.get(),self.temp))
        self.row6=self.mycurson1.fetchone()
        self.row10=(str(self.row6))
        if self.row6 != None:
            self.a3.bind("<Button-1>")
            self.a3.place_forget()
            self.btn3.bind("<Button-1>")
            self.btn3.place_forget()
            self.la4=Label(win,text="DepositAMT",font=('Calibri 15'))
            self.la4.place(x=220,y=95)
            self.b2=Entry(win,width=35)
            self.b2.place(x=350,y=100)
            self.Btn4=Button(win,text="proceed",command=self.final2)
            self.Btn4.place(x=380,y=120)
        else:
            self.a3.bind("<Button-1>")
            self.a3.place_forget()
            self.btn3.bind("<Button-1>")
            self.btn3.place_forget()
            self.Alert()

    def hide_me1(self, event):
        
        print('hide me')
        event.widget.place_forget()
        self.withdraw()
        
    def final(self):
        self.la1.bind("<Button-1>")
        self.la1.place_forget()
        self.t2=int(self.b.get())
        self.b.bind("<Button-1>")
        self.b.place_forget()
        self.Btn2.bind("<Button-1>")
        self.Btn2.place_forget()
        s10=""
        for i in self.row2:
            if i=='(' or  i==')' or i==',':
                continue
            else:
                s10=s10+i
                
        self.x4=int(s10)
        self.x2=int(self.b.get())
        self.x3=self.x4-self.x2
        self.x5=str(self.x3)
        print(self.x3)
        self.c1=self.mydb.cursor()
        self.c1.execute("update s1 set salary=%s where id=%s",(self.x5,self.a3.get()))
        self.mydb.commit()
        #self.initial()
        win.destroy()
    def initial(self):
        self.c2=self.mydb.cursor()
        self.c2.execute("select salary from s1 where id=%s and temp=%s",(self.a3.get(),self.temp))
        self.y=self.c2.fetchone()
        self.y2=str(self.y)
        s11=""
        for i in self.y2:
            if i=='(' or  i==')' or i==',':
                continue
            else:
                s11=s11+i
        self.y1=int(s11)
        self.la2=Label(win,text="Balance:",font=('Calibri 15'))
        self.la2.place(x=250,y=180)
        labe3=Label(win, text="Balance: ", font=('Calibri 15'))
        labe3.place(x=350,y=180)
        labe3.config(text=self.y1)
    def initial2(self):

        self.la5=Label(win,text="Balance:",font=('Calibri 15'))
        self.la5.place(x=250,y=180)
        labe6=Label(win, text="Total: ", font=('Calibri 15'))
        labe6.place(x=350,y=180)
        labe6.config(text=self.Amount)
        
    def hide_me2(self, event):
        
        print('hide me')
        event.widget.place_forget()
        self.deposit()
    
    def final2(self):
        self.la4.bind("<Button-1>")
        self.la4.place_forget()
        self.b2.bind("<Button-1>")
        self.b2.place_forget()
        self.Btn4.bind("<Button-1>")
        self.Btn4.place_forget()
        s12=""
        for i in self.row10:
            if i=='(' or  i==')' or i==',':
                continue
            else:
                s12=s12+i
                
        self.x7=int(s12)
        self.x8=int(self.b2.get())
        self.x9=self.x7+self.x8
        self.x10=str(self.x9)
        print(self.x9)
        self.c3=self.mydb.cursor()
        self.c3.execute("update s1 set salary=%s where id=%s",(self.x10,self.a3.get()))
        self.mydb.commit()
        win.destroy()
        #self.initial2()
    def entered(self,event):
        self.std.config(bg="#000000",fg="#ffffff")
    def left(self,event):
        self.std.config(bg='light blue',fg='#000000')
    def entered1(self,event):
        self.std4.config(bg="#000000",fg="#ffffff")
    def left1(self,event):
        self.std4.config(bg='light blue',fg='#000000')
    def entered2(self,event):
        self.std2.config(bg="#000000",fg="#ffffff")
    def left2(self,event):
        self.std2.config(bg='light blue',fg='#000000')
    def entered3(self,event):
        self.std3.config(bg="#000000",fg="#ffffff")
    def left3(self,event):
        self.std3.config(bg='light blue',fg='#000000')

from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("ATM_GUI_APPLICATION")
#root.title("Title")

#img = Image.open(r'C:\shiva_test\Train_images\bg_image2.png')
"""bg = ImageTk.PhotoImage(file=r'C:\shiva_test\Train_images\image3.jpg',master=win)

lbl = Label(win,image=bg)
lbl.pack()"""
win.geometry("750x550")
f= Frame(win,background='grey')
f.pack(expand=True,fill=BOTH)

  
# Display image

#win.attributes('-alpha',0.5)
#win.configure(bg='light blue')
b=atm(win)




win.mainloop()
 


