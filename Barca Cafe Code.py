from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image  
import datetime
import time


root = tk.Tk()
root.title('BARCA CAFE')
root.geometry('1500x750')
root.configure(background="#000099")
root.resizable(False , False)
root.iconbitmap("D:\\Learn\\Projects\\الصباغ\\ttt.ico")


fnt = ("tahoma" , 30)
fnt1 = ("tahoma" , 20)
fnt2 = ("tahoma" , 19)

lbl = tk.Label(root , text = "BARCA CAFE" , bg = "yellow"  , font = fnt)
lbl.place(relx = 0.3 , rely = 0.01, relwidth = 0.4 , relheight = 0.1)
#####################################################################
image1 = Image.open("D:\\Learn\\Projects\\الصباغ\\rrr.png")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.place(x=10, y=480)

image2 = Image.open("D:\\Learn\\Projects\\الصباغ\\barca.png")
test1 = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=test1)
label2.image = test
label2.place(x=865, y=480)
#####################################################################

frame1 = tk.Frame(root , bg = "red", bd = 10)
frame1.place( relx = 0.87 , rely = 0.14 , relwidth =0.24 , relheight = 0.8 ,  anchor = "n" )

lbl = tk.Label(frame1  , width = 15 , text = "Orders" , bg = "yellow", font=('Helvetica 15 bold'))
lbl.place(x = 90 , y = 0 , relheight = 0.099)

lbl2 = tk.Label(frame1  , width = 15 , text = "Total Orders :" , bg = "yellow", font=('Helvetica 15 bold'))
lbl2.place(x = 0 , y = 65 , relheight = 0.89, relwidth=1)
#####################################################################



prices = {
    "Tea" : 10,
    "Tea With Milk" : 15,
    "Tea With Lemon" : 18,
    "Sa7lb":30,
    "Yansoon":25,
    "Coffee":18,
    "Black Coffee":20,
    "Turkish Coffee":30,
    "French Coffee":35,
    "American Coffee":35,
    "Manga":40,
    "Strawberry":45,
    "Watermelon":45,
    "Orange":45,
    "Lemon":35,
    "Pepsi":25,
    "Schweppes":25,
    "7UP":25,
    "Cocacola":25,
    "RedBull":45,
    "waffle":55,
    "moltencake":55,
    "cheesecake":65,
    "pancake":60,
    "cookie":55

    }
#####################################################################

calc = 0
orders = []

#Tea
def buttonteaclick():
    print("ONE TEA = " + str(prices["Tea"]))
    orders.append("ONE Tea = {} ".format(str(prices["Tea"])))
    global calc 
    calc += prices["Tea"]


def buttonTeawithMilkclick():
    print("ONE Tea With Milk = " + str(prices["Tea With Milk"]))
    orders.append("ONE Tea With Milk = {} ".format(str(prices["Tea With Milk"])))
    global calc 
    calc += prices["Tea With Milk"]

def buttonTeawithlemonclick():
    print("ONE Tea With Lemon = " + str(prices["Tea With Lemon"]))
    orders.append("ONE Tea With Lemon = {} ".format(str(prices["Tea With Lemon"])))
    global calc 
    calc += prices["Tea With Lemon"]

#Other
    
def buttonsa7lbclick():
    print("ONE Sa7lb = " + str(prices["Sa7lb"]))
    orders.append("ONE Sa7lb = {} ".format(str(prices["Sa7lb"])))
    global calc 
    calc += prices["Sa7lb"]
    
    
def buttonYansoonclick():
    print("ONE Yansoon = " + str(prices["Yansoon"]))
    orders.append("ONE Yansoon = {} ".format(str(prices["Yansoon"])))
    global calc 
    calc += prices["Yansoon"]

#Coffee

def buttoncoffeeclick():
    print("ONE Coffee = " + str(prices["Coffee"]))
    orders.append("ONE Coffee = {} ".format(str(prices["Coffee"])))
    global calc 
    calc += prices["Coffee"]
    
def buttonBlackcoffeeclick():
    print("ONE Black Coffee = " + str(prices["Black Coffee"]))
    orders.append("ONE Black Coffee = {} ".format(str(prices["Black Coffee"])))
    global calc 
    calc += prices["Black Coffee"]

def buttonTurkishcoffeeclick():
    print("ONE Turkish Coffee = " + str(prices["Turkish Coffee"]))
    orders.append("ONE Turkish Coffee = {} ".format(str(prices["Turkish Coffee"])))
    global calc 
    calc += prices["Turkish Coffee"]

def buttonFrenchcoffeeclick():
    print("ONE French Coffee = " + str(prices["French Coffee"]))
    orders.append("ONE French Coffee = {} ".format(str(prices["French Coffee"])))
    global calc 
    calc += prices["French Coffee"]

def buttonAmericancoffeeclick():
    print("ONE American Coffee = " + str(prices["American Coffee"]))
    orders.append("ONE American Coffee = {} ".format(str(prices["American Coffee"])))
    global calc 
    calc += prices["American Coffee"]

#Juices    
def buttonmangaclick():
    print("ONE Manga = " + str(prices["Manga"]))
    orders.append("ONE Manga = {} ".format(str(prices["Manga"])))
    global calc 
    calc += prices["Manga"]
    
def buttonStrawberryclick():
    print("ONE Strawberry = " + str(prices["Strawberry"]))
    orders.append("ONE Strawberry = {} ".format(str(prices["Strawberry"])))
    global calc 
    calc += prices["Strawberry"]
    
def buttonwatermelonclick():
    print("ONE Watermelon = " + str(prices["Watermelon"]))
    orders.append("ONE Watermelon = {} ".format(str(prices["Watermelon"])))
    global calc 
    calc += prices["Watermelon"]
    
def buttonorangeclick():
    print("ONE Orange = " + str(prices["Orange"]))
    orders.append("ONE Orange = {} ".format(str(prices["Orange"])))
    global calc 
    calc += 35
    
def buttonLemonclick():
    print("ONE Lemon = " + str(prices["Lemon"]))
    orders.append("ONE Lemon = {} ".format(str(prices["Lemon"])))
    global calc 
    calc += prices["Lemon"]

#Soft drinks

def buttonpepsiclick():
    print("ONE Pepsi = " + str(prices["Pepsi"]))
    orders.append("ONE Pepsi = {} ".format(str(prices["Pepsi"])))
    global calc 
    calc += prices["Pepsi"]
    
def buttonschweppesclick():
    print("ONE Schweppes = " + str(prices["Schweppes"]))
    orders.append("ONE Schweppes = {} ".format(str(prices["Schweppes"])))
    global calc 
    calc += prices["Schweppes"]
    
def button7UPlick():
    print("ONE 7UP = " + str(prices["7UP"]))
    orders.append("ONE 7UP = {} ".format(str(prices["7UP"])))
    global calc 
    calc += prices["RedBull"]
    
def buttoncocacolaclick():
    print("ONE Cocacola = " + str(prices["Cocacola"]))
    orders.append("ONE Cocacola = {} ".format(str(prices["Cocacola"])))
    global calc 
    calc += prices["Cocacola"]
    
def buttonredbullclick():
    print("ONE RedBull = " + str(prices["RedBull"]))
    orders.append("ONE RedBull = {} ".format(str(prices["RedBull"])))
    global calc 
    calc += prices["RedBull"]

#dessert
def buttonwaffleclick():
    print("ONE waffle = " + str(prices["waffle"]))
    orders.append("ONE waffle = {} ".format(str(prices["waffle"])))
    global calc 
    calc += prices["waffle"]

def buttonmoltencakeclick():
    print("ONE moltencake = " + str(prices["moltencake"]))
    orders.append("ONE moltencake = {} ".format(str(prices["moltencake"])))
    global calc 
    calc += prices["moltencake"]

def buttoncheesecakeclick():
    print("ONE cheesecake = " + str(prices["cheesecake"]))
    orders.append("ONE cheesecake = {} ".format(str(prices["cheesecake"])))
    global calc 
    calc += prices["cheesecake"]

def buttonpancakeclick():
    print("ONE pancake = " + str(prices["pancake"]))
    orders.append("ONE pancake = {} ".format(str(prices["pancake"])))
    global calc 
    calc += prices["cookie"]

def buttoncookieclick():
    print("ONE cookie = " + str(prices["cookie"]))
    orders.append("ONE cookie = {} ".format(str(prices["cookie"])))
    global calc 
    calc += prices["cookie"]





#Tea
buttontea = tk.Button(root,text="Tea",font = fnt2,background = "red"
                ,command = buttonteaclick )
buttontea.place(relx = 0.006 , rely  = 0.14 , relwidth = 0.14 , relheight = 0.08)


buttonTeawithmilk = tk.Button(root,text="Tea With Milk",font = fnt2,background = "red",command = buttonTeawithMilkclick )
buttonTeawithmilk.place(relx = 0.155 , rely  = 0.14 , relwidth = 0.14 , relheight = 0.08)

buttonTeawithlemon = tk.Button(root,text="Tea With Lemon",font = fnt2,background = "red",command = buttonTeawithlemonclick)
buttonTeawithlemon.place(relx = 0.304 , rely  = 0.14 , relwidth = 0.14 , relheight = 0.08)


#Other

buttonsa7lb = tk.Button(root,text="Sa7lb",font = fnt2,background = "red" , command = buttonsa7lbclick)
buttonsa7lb.place(relx = 0.453 , rely  = 0.14 , relwidth = 0.14 , relheight = 0.08)

buttonYansoon = tk.Button(root,text="Yansoon",font = fnt2,background = "red" , command = buttonYansoonclick)
buttonYansoon.place(relx =0.602 , rely  = 0.14 , relwidth = 0.14 , relheight = 0.08)


#Coffee

buttoncoffee = tk.Button(root,text="Coffee",font = fnt2,background = "red" , command = buttoncoffeeclick)
buttoncoffee.place(relx = 0.006 , rely  = 0.24 , relwidth = 0.14 , relheight = 0.08)

buttonBlackcoffee = tk.Button(root,text="Black Coffee",font = fnt2,background = "red" , command = buttonBlackcoffeeclick)
buttonBlackcoffee.place(relx = 0.155     , rely  = 0.24 , relwidth = 0.14 , relheight = 0.08)

buttonTurkishcoffee = tk.Button(root,text="Turkish Coffee",font = fnt2,background = "red" , command = buttonTurkishcoffeeclick )
buttonTurkishcoffee.place(relx = 0.304 , rely  = 0.24 , relwidth = 0.14 , relheight = 0.08)

buttonFrenchcoffee = tk.Button(root,text="French Coffee",font = fnt2,background = "red" , command = buttonFrenchcoffeeclick)
buttonFrenchcoffee.place(relx = 0.453, rely  = 0.24 , relwidth = 0.14 , relheight = 0.08)

buttonAmericancoffee = tk.Button(root,text="American Coffee",font = fnt2,background = "red" , command = buttonAmericancoffeeclick )
buttonAmericancoffee.place(relx = 0.602 , rely  = 0.24 ,relwidth = 0.14 , relheight = 0.08)

#Juices

buttonmanga = tk.Button(root,text="Manga",font = fnt2,background = "red" , command = buttonmangaclick)
buttonmanga.place(relx = 0.006 , rely  = 0.34 , relwidth = 0.14 , relheight = 0.08)

buttonStrawberry = tk.Button(root,text="Strawberry",font = fnt2,background = "red" , command = buttonStrawberryclick)
buttonStrawberry.place(relx = 0.155, rely  = 0.34 , relwidth = 0.14 , relheight = 0.08)

buttonwatermelon = tk.Button(root,text="Watermelon",font = fnt2,background = "red" , command = buttonwatermelonclick)
buttonwatermelon.place(relx = 0.304, rely  = 0.34 , relwidth = 0.14 , relheight = 0.08)

buttonorange = tk.Button(root,text="Orange",font = fnt2,background = "red" ,command = buttonorangeclick)
buttonorange.place(relx = 0.453, rely  = 0.34 , relwidth = 0.14 , relheight = 0.08)

buttonLemon = tk.Button(root,text="Lemon",font = fnt2,background = "red" , command = buttonLemonclick)
buttonLemon.place(relx = 0.602, rely  = 0.34 , relwidth = 0.14 , relheight = 0.08)

#Soft drinks

buttonpepsi = tk.Button(root,text="Pepsi",font = fnt2,background = "red", command = buttonpepsiclick)
buttonpepsi.place(relx = 0.006 , rely  = 0.44 , relwidth = 0.14 , relheight = 0.08)

buttonschweppes = tk.Button(root,text="Schweppes",font = fnt2,background = "red" , command = buttonschweppesclick )
buttonschweppes.place(relx = 0.155 , rely  = 0.44 , relwidth = 0.14 , relheight = 0.08)

button7UP = tk.Button(root,text="7UP",font = fnt2,background = "red" ,command =button7UPlick )
button7UP.place(relx = 0.304 , rely  = 0.44 , relwidth = 0.14 , relheight = 0.08)

buttoncocacola = tk.Button(root,text="Cocacola",font = fnt2,background = "red", command = buttoncocacolaclick)
buttoncocacola.place(relx = 0.453 , rely  = 0.44 , relwidth = 0.14 , relheight = 0.08)

buttonredbull = tk.Button(root,text="Red Bull",font = fnt2,background = "red",command = buttonredbullclick)
buttonredbull.place(relx = 0.602 , rely  = 0.44 , relwidth = 0.14 , relheight = 0.08)


#desserts
buttontea = tk.Button(root,text="waffle",font = fnt2,background = "red"
                ,command = buttonwaffleclick )
buttontea.place(relx = 0.006 , rely  = 0.54 , relwidth = 0.14 , relheight = 0.08)

buttontea = tk.Button(root,text="moltencake",font = fnt2,background = "red"
                ,command = buttonmoltencakeclick )
buttontea.place(relx = 0.155 , rely  = 0.54 , relwidth = 0.14 , relheight = 0.08)

buttontea = tk.Button(root,text="cheesecake",font = fnt2,background = "red"
                ,command = buttoncheesecakeclick )
buttontea.place(relx = 0.304 , rely  = 0.54 , relwidth = 0.14 , relheight = 0.08)

buttontea = tk.Button(root,text="pancake",font = fnt2,background = "red"
                ,command = buttonpancakeclick )
buttontea.place(relx = 0.453 , rely  = 0.54 , relwidth = 0.14 , relheight = 0.08)

buttontea = tk.Button(root,text="cookie",font = fnt2,background = "red"
                ,command = buttoncookieclick )
buttontea.place(relx = 0.602 , rely  = 0.54 , relwidth = 0.14 , relheight = 0.08)










def clear():
    global calc
    global orders
    calc = 0
    orders = []


button3= tk.Button(root, font = 15 , bg = "red" , text = "Clear")
button3.place(relx = 0.2 , rely = 0.7 ,relwidth = 0.14 , relheight = 0.08)
button3.config(command = clear)




def total():
    print("Total : "+str(calc))
    print(orders)
    allorders = "\n".join(orders)
    lbl2['text'] = "All of Orders : \n" + allorders
    result = tk.Label(root , text = "Total : " + str(calc) , bg = "yellow"  , font = fnt)
    result.place(relx = 0.39 , rely = 0.8, relwidth = 0.14 , relheight = 0.08)

buttontotal= tk.Button(root,text="Total",font = fnt2,background = "red",command = total)
buttontotal.place(relx = 0.39 , rely  = 0.7 , relwidth = 0.14 , relheight = 0.08)


button2 = tk.Button(root, font = 15 , bg = "red" , text = "Exit Now!")
button2.place(relx = 0.2 , rely = 0.8 ,relwidth = 0.14 , relheight = 0.08)
button2.config(command = root.destroy)


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        } 


datef = tk.Label(root, text=day + "-" + mont[month] + "-" + year , fg="orange", 
                 width=18, height=2,font=('times',15, ' bold '))
datef.place( x = 30 , y = 25)

clock = tk.Label(root, fg="red",  width=10, height=2, font=('times', 15, ' bold '))
clock.place( x = 250, y = 25)
tick()



root.mainloop()

