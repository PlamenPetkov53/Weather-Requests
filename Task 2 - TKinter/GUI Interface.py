from tkinter import *
import  tkinter as tk
import  re
import requests
import json
import  DefWEatherRequests
class MyWindow:


    def __init__(self, win):
        self.lbl1=Label(win, text='Enter Cities')
        self.t1 = Entry(win, width="50")
        self.t1.grid(row=0, column=1, padx=5, pady=10, ipady=3)
        self.t4 = Entry(win, width="50")
        self.t4.grid(row=0, column=1, padx=5, pady=10, ipady=3)
        self.t5 = Entry()
        self.t6 = Entry()
        self.t7 = Entry(win, width="80")
        self.t7.grid(row=0, column=1, padx=5, pady=10, ipady=3)
        self.t8 = Entry()
        self.t9 = Entry()
        self.btn1 = Button(win, text='Request')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(win, text='Request', command=self.add)
        self.b2=Button(win, text='smth')
        self.b1.place(x=100, y=150)
        self.lbl4 = Label(win, text='Name of Citie/s')
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)
        self.lbl5 = Label(win, text='Current temperature (celsius)')
        self.lbl5.place(x=30, y=300)
        self.t5.place(x=200, y=300)
        self.lbl6 = Label(win, text='Current humidity (%)')
        self.lbl6.place(x=65, y=350)
        self.t6.place(x=200, y=350)
        self.lbl7 = Label(win, text='The sky is:')
        self.lbl7.place(x=100, y=400)
        self.t7.place(x=200, y=400)
        self.lbl8 = Label(win, text='Minimum temperature is:')
        self.lbl8.place(x=50, y=450)
        self.t8.place(x=200, y=450)
        self.lbl8 = Label(win, text='Average temperature is:')
        self.lbl8.place(x=50, y=500)
        self.t9.place(x=200, y=500)

    def add(self):
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)
        self.t9.delete(0, END)
        inpt = None
        user_input=self.t1.get()
        coldest_city = []
        inpt = re.findall(r"[\w']+", user_input)

        if len(inpt) == 1:
            OneCity = DefWEatherRequests.WeatherRequests.search_for_one_city(self, inpt, self.t4, self.t5, self.t6,
                                                                             self.t7, self.t8, self.t9)
        else:
            FiveCities = DefWEatherRequests.WeatherRequests.search_for_five_cities(self, inpt, self.t4, self.t5,
                                                                                   self.t6, self.t7, self.t8, self.t9)



window=Tk()
mywin=MyWindow(window)
window.title('WeatherRequest')
window.geometry("720x650+10+10")
window.mainloop()
