from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

mrksht=sqlite3.connect("marks.db")
c=mrksht.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS MARK (roll int,name text,maths float,science float,social float)""")
mrksht.commit()
mrksht.close()

def insert ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (tab):
            messagebox.showerror("Error","Already exists")
      else:
            if (n1.get()=="" or n2.get()=="" or n3.get()=="" or n4.get()=="" or n5.get()==""):
                  messagebox.showerror("Error","Enter the data first")
            if (int(n3.get())>100 or int(n4.get())>100 or int(n5.get())>100):
                  messagebox.showerror("Error","mark exeeds 100-limit")
            else:
                  c.execute("INSERT INTO MARK VALUES (:roll,:name,:maths,:science,:social)",{'roll':n1.get(),'name':n2.get(),'maths':n3.get(),'science':n4.get(),'social':n5.get()})
                  messagebox.showinfo("Info","inserted succesfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
                  n4.delete(0,END)
                  n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def search ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      n2.delete(0,END)
      n3.delete(0,END)
      n4.delete(0,END)
      n5.delete(0,END)
      if (not tab):
            messagebox.showerror("Error","Not found")
      else:
           n2.insert(END,str(tab[0][1]))
           n3.insert(END,str(tab[0][2]))
           n4.insert(END,str(tab[0][3]))
           n5.insert(END,str(tab[0][4]))
      mrksht.commit()
      mrksht.close()

def update ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            c.execute('''UPDATE MARK set roll=:q,name=:r,maths=:n,science=:b,social=:v WHERE roll=:q''',{'q':s,'r':n2.get(),'n':n3.get(),'b':n4.get(),'v':n5.get()})
            messagebox.showinfo("info","Updated succesfully")
      n1.delete(0,END)
      n2.delete(0,END)
      n3.delete(0,END)
      n4.delete(0,END)
      n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def delete ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            msg=messagebox.askquestion("Delete","Are you sure to delete??")
            if(msg=="yes"):
                  c.execute("DELETE FROM MARK WHERE roll='"+s+"'")
                  messagebox.showinfo("Info","Deleted sucessfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
                  n4.delete(0,END)
                  n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def view ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      c.execute("SELECT * FROM MARK")
      tab=c.fetchall()
      for row in viewtrv.get_children():
            viewtrv.delete(row)
      k=0
      for s in tab:
            l=[]
            l.append(tab[k][0])
            l.append(tab[k][1])
            m=tab[k][2]
            s=tab[k][3]
            ss=tab[k][4]
            tm=int(s+ss+m)
            av=int(tm/3)
            if (av>=90):
                  grade="A"
            elif (av>=70):
                  grade="B"
            elif (av>=40):
                  grade="C"
            else:
                  grade="D"
            l.append(m)
            l.append(s)
            l.append(ss)
            l.append(tm)
            l.append(grade)
            viewtrv.insert("",END,values=l)
            k=k+1
      mrksht.commit()
      mrksht.close()
      
win=Tk()
win.title("Mark register---TARUNJEETH(PYTN-A1 22-23)")
win.iconbitmap(r"unnamed.ico")
file="./logo.png"
img=PhotoImage(file=file)
labimg=Label(win,image=img)
labimg.grid(row=0,column=3)
labimg.image=img
labl=Label(win,text="roll no")
labl.grid(row=0,column=0)
n1=Entry(win,width=70)
n1.grid(row=0,column=1)
labl1=Label(win,text="name of the student")
labl1.grid(row=1,column=0)
n2=Entry(win,width=70)
n2.grid(row=1,column=1)
labl2=Label(win,text="maths mark")
labl2.grid(row=2,column=0)
n3=Entry(win,width=70)
n3.grid(row=2,column=1)
labl3=Label(win,text="science mark")
labl3.grid(row=3,column=0)
n4=Entry(win,width=70)
n4.grid(row=3,column=1)
labl4=Label(win,text="social mark")
labl4.grid(row=4,column=0)
n5=Entry(win,width=70)
n5.grid(row=4,column=1)
but=Button(win,text="insert",command=insert)
but.grid(row=5,column=0)
but1=Button(win,text="view",command=view)
but1.grid(row=5,column=1)
but2=Button(win,text="search",command=search)
but2.grid(row=5,column=2)
but3=Button(win,text="update",command=update)
but3.grid(row=5,column=3)
but4=Button(win,text="delete",command=delete)
but4.grid(row=5,column=4)
viewtrv=ttk.Treeview(win,columns=("c1","c2","c3","c4","c5","c6","c7"),show="headings")
viewtrv.grid(row=6,column=0,columnspan=5)
viewtrv.heading("#1",text="roll no")
viewtrv.heading("#2",text="Student name")
viewtrv.heading("#3",text="Maths mark")
viewtrv.heading("#4",text="Science mark")
viewtrv.heading("#5",text="Social mark")
viewtrv.heading("#6",text="Total marks")
viewtrv.heading("#7",text="grade")
labltxt=Label(win,text="With 💖 ,Tarunjeeth PYTN-A1",font="77")
labltxt.grid(row=7,column=0)
win.mainloop()
