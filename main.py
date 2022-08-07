from tkinter import*
import tkinter.messagebox as msg
import mysql.connector
class First:
    def __init__(self):
        window=Tk()
        b1=Button(window,text="Store Books",command=self.bookstorage)
        b1.place(x=20,y=40)
        b2 = Button(window,text="Search books",command=self.bookenquiry)
        b2.place(x=20,y=80)
        window.mainloop()

    def bookstorage(self):
        store_window=Tk()
        store_window.geometry("500x400")
        name=Label(store_window,text="Book Name")
        name.place(x=10,y=50)
        self.n_l=Entry(store_window)
        self.n_l.place(x=80,y=50)

        author=Label(store_window,text="author Name")
        author.place(x=10,y=100)
        self.a_l=Entry(store_window)
        self.a_l.place(x=80,y=100)

        quantity = Label(store_window, text="No of Books")
        quantity.place(x=10, y=150)
        self.e_l = Entry(store_window)
        self.e_l.place(x=80,y=150)
        
        sb=Button(store_window,text="submit", command=self.connect)
        sb.place(x=150,y=180)

        store_window.mainloop()
        
    def connect(self):
        mydb=mysql.connector.connect(host="localhost",user="root",port=3306,password="Mouli$345",database="Bookstore")
        mycursor=mydb.cursor()
        Bookname=self.n_l.get()
        Author=self.a_l.get()
        Quantity=self.e_l.get()
        mycursor.execute("insert into storage values(%s,%s,%s)",(Bookname,Author,Quantity))
        mydb.commit()
        msg.showinfo("Bookstore","The stock has been updated")

    def bookenquiry(self):
        enquiry_window = Tk()
        enquiry_window.geometry("500x400")
        name = Label(enquiry_window, text="Book Name")
        name.place(x=10, y=50)
        self.b_l = Entry(enquiry_window)
        self.b_l.place(x=80, y=50)

        author = Label(enquiry_window, text="author name")
        author.place(x=10, y=100)
        self.q_l = Entry(enquiry_window)
        self.q_l.place(x=110, y=100)

        sb = Button(enquiry_window, text="submit", command=self.enquiry_data)
        sb.place(x=150, y=180)

        enquiry_window.mainloop()

    def enquiry_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", port=3306, password="Mouli$345",database="Bookstore")
        mycursor = mydb.cursor()
        bookname = self.b_l.get()
        author = self.q_l.get()
        mycursor.execute("select quantity from storage where Bookname=%s and author=%s",(bookname,author))
        y = 0
        for i in mycursor:
            y = int(i[0])
        if y>=1:
            y=y-1
            mycursor.execute("Update storage set quantity=%s where Bookname=%s and author=%s",(y,bookname,author))
            mycursor.execute("insert into  enquiry_books values(%s,%s)",(bookname,author))
            mydb.commit()
            msg.showinfo("Book Availability", "Stock Available")
        else:
            msg.showerror("Book Availability", "No stock Available")                             
        
f=First()