
from tkinter import *
from tkinter import Tk,ttk
import requests
import json

Gui = Tk()
Gui.geometry('400x420')
Gui.title('โปรแกรมแปลงสกุลเงิน')
Gui.resizable(height=FALSE,width=FALSE)
img = PhotoImage(file = 'C:\\Users\\comp514\\Pictures\\Saved Pictures\\money-bag.png')
Gui.iconphoto(False,img)

currency = ['THB','USD','GBP','EUR','JPY','HKD','MYR','SGD','BND','PHP','IDR','INR','CHF','AUD','NZD','CAD','SEK','DKK','NOK','CNY','MXN','ZAR','KRW','TWD','KWD','SAR','AED','MMK','BDT','CZK','KHR','KES','LAK','RUB','VND','EGP','PLN','LKR','IQD','BHD','OMR','JOD','QAR','MVR','NPR','PGK','ILS','HUF','PKR']

# function คำนวน
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combobox1.get()
    currency_2 = combobox2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	    "X-RapidAPI-Key": "724cd62392msh0fb93f0428fdf19p1edcecjsnfa52cd4b3b83",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    data = json.loads(response.text)

    converted_amount = data['result']['convertedAmount']

    formatted = "{:,.3f}".format(converted_amount)

    result['text'] = formatted

# ส่วนหัว
top = Frame(Gui, width = 550,height = 100,bg = '#2B32B2')
top.grid(row=0,column=0)

programname = Label(text='Ninthai Convert Money',anchor=CENTER,font=('Arial 15 bold'),fg = '#86fde8',bg = '#2B32B2')
programname.place(x=90,y=40)

# ส่วนตรงกลาง
maintop = Frame(Gui, width = 550,height = 400,bg = '#292E49')
maintop.grid(row=1,column=0)

# หน้าจอตรงแสดงผลลัพธ์
result = Label(text='', width=20, height=3,pady=10, relief='solid',anchor=CENTER,font=('Ivy 13 bold'),fg = 'black',bg = 'white')
result.place(x= 95 , y = 115 )

# ที่ใส่ข้อมูลอั่นแรก
combobox1 = ttk.Combobox(maintop,width=12,height=15,justify = CENTER,font=('Ivy 12 bold'))
combobox1['values'] = (currency)
combobox1.place(x=30,y=140)

first1 = Label(text='ค่าเงินแรก',anchor=CENTER,font=('Arial 15 bold'),fg = '#86fde8',bg = '#292E49')
first1.place(x=30,y=200)

# ที่ใส่ข้อมูลอั่นที่สอง
combobox2 = ttk.Combobox(maintop,width=12,height=15,justify = CENTER,font=('Ivy 12 bold'))
combobox2['values'] = (currency)
combobox2.place(x=30,y=210)

first2 = Label(text='จะเปลี่ยนเป็น',anchor=CENTER,font=('Arial 15 bold'),fg = '#86fde8',bg = '#292E49')
first2.place(x=30,y=275)

# ที่ใส่ข้อมูลจำนวนเงิน
value = Entry(maintop,width=25,justify=CENTER,font=('Ivy 12 bold'),relief='solid')
value.place(x=85,y = 280)

first3 = Label(text='จำนวนเงิน',anchor=CENTER,font=('Arial 15 bold'),fg = '#86fde8',bg = '#292E49')
first3.place(x=155,y=345)

# ปุ่มเปลี่ยนค่า
button = Button(maintop,text='กดปุ่มเพื่อเปลี่ยนค่า',width=14,padx=10,height=4,bg = '#acb6e5',fg = '#2B32B2',font = ('Ivy 15 bold'),command=convert)
button.place(x=195,y=120)

Gui.mainloop()