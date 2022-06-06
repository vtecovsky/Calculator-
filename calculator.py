from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


main = Tk()
main.title('Многофункциональный калькулятор')
main.geometry('400x250')
main.resizable(False, False)

def click1():
    a = int(koren_ent1.get())**(1/2)
    try:
        res['text'] = str(a)
    except: mb.showerror('Ошибка', 'Неверные данные!')
def click2():
    a = int(koren_ent2.get())**(1/3)
    try:
        res1['text'] = str(a)
    except: mb.showerror('Ошибка', 'Неверные данные!')
def plus():
    n1=int(e1.get())
    n2=int(e2.get())
    sum1=n1+n2
    t1.config(text=str(sum1))
def minus():
    n1=int(e1.get())
    n2=int(e2.get())
    min1=n1-n2
    t1.config(text=str(min1))
def ymn():
    n1=int(e1.get())
    n2=int(e2.get())
    ymn1=n1*n2
    t1.config(text=str(ymn1))
def del1():
    n1=int(e1.get())
    n2=int(e2.get())
    if n2==0:
        mb.showerror('Ошибка', 'Делить на 0 нельзя')
    else:
        del1=n1/n2
    t1.config(text=str(del1))

rows = 0
while rows < 40:
    main.rowconfigure(rows, weight = 1)
    main.columnconfigure(rows, weight = 1)
    rows += 1

note = ttk.Notebook(main)
note.grid(row=1, column=0, columnspan=40, rowspan=39, sticky='NESW')

page1 = ttk.Frame(note)
note.add(page1, text='Корни n-ой степени')
face = Label(page1, text='Корни 2 и 3 степени', font=('Consolas', 15, 'bold')).pack()
koren_label = Label(page1, text='Корень 2 степени: ').pack()
res = Label(page1, text='0', font=('Consolas', 10, 'bold'))
res.pack()
koren_ent1 = Entry(page1, text='', font=('Consolas', 10))
koren_ent1.pack()
Button(page1, text='Решить', font=('Consolas', 10), command=click1).pack()

koren_label = Label(page1, text='Корень 3 степени: ').pack()
res1 = Label(page1, text='0', font=('Consolas', 10, 'bold'))
res1.pack()
koren_ent2 = Entry(page1, text='', font=('Consolas', 10))
koren_ent2.pack()
Button(page1, text='Решить', font=('Consolas', 10), command=click2).pack()


page2 = ttk.Frame(note)
note.add(page2, text='Простейшие операции')
t1=Label(page2,  text='Введите два числа', font=('Consolas', 15, 'bold'))
t1.pack()
e1=Entry(page2,width=25)
e1.pack()
e2=Entry(page2,width=25)
e2.pack()
b1=Button(page2,text="+", command=plus)
b1.pack()
b1=Button(page2,text="-", command=minus)
b1.pack()
b1=Button(page2,text="*", command=ymn)
b1.pack()
b1=Button(page2,text="/", command=del1)
b1.pack()


page3 = ttk.Frame(note)
A=Label(page3,  text='Корень 3 степени:', font=('Consolas', 15, 'bold'))

main.mainloop()