from tkinter import *
import datetime

pencere = Tk()
pencere.geometry('300x150+50+100')
pencere.title('Saat Uygulamasi')
pencere.tk_setPalette("#D0A9F5")


def saatal():
      saat=datetime.datetime.now()
      saatt=datetime.datetime.strftime(saat,'%H:%M:%S')      
      return saatt
def goster():
      etiket["text"]=saatal()
def kapat():
      etiket["text"]="Saat Kac?"

etiket = Label(text='Saat Kac?',
               bg='light pink',
               fg='black',
               font='Helvetica 12 bold',
               width=8, height=1,
               bd=10, relief=SUNKEN)
etiket.pack(expand=YES)

button1 = Button(text='Goster',
            bg='green',
            fg='white',
            font='Times 12 bold',
            cursor='heart',
            width=10, height=0,
            bd=5, relief=GROOVE,
            command=goster)
button1.pack(side=LEFT,expand=YES)

button2 = Button(text='Kapat',
               bg='red',
               fg='white',
               font='Times 12 bold',
               cursor='cross',
               width=10, height=0,
            bd=5, relief=GROOVE,
               command=kapat)
button2.pack(side=LEFT,expand=YES)

pencere.mainloop()



