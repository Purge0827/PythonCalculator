from tkinter import *
window = Tk()

window.geometry('366x470')

window.title('Calculator')

window.configure(bg='#A9A9A9')

window.wm_resizable(False,False)

expression= ''
def press(num):
  global expression

  expression = expression + str(num)

  equation.set(expression)

def equalpress():
  global expression

  try:
      total = str(eval(expression))

      equation.set(total)

      expression = ''
  except:
      equation.set("Error Occurred")
      expression = ''
def clear():
  global expression

  expression = ''
  equation.set('0')

button_frame = Frame(window,bg='#A9A9A9')
button_frame.pack()

equation = StringVar()
expression_field = Entry(button_frame,textvariable=equation,
              justify='right',font=('arial',20,'bold'))

button1 = Button(button_frame,text='1',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(1))

button2 = Button(button_frame,text='2',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(2))

button3 = Button(button_frame,text='3',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(3))

addition = Button(button_frame,text='+',font=('times new roman',12),relief='ridge',
          bd=1,bg='#FF8C00',width=8,height=3,command=lambda:press('+'))

button4 = Button(button_frame,text='4',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(4))

button5 = Button(button_frame,text='5',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(5))

button6 = Button(button_frame,text='6',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(6))

subtract = Button(button_frame,text='-',font=('times new roman',12),relief='ridge',
          bd=1,bg='#FF8C00',width=8,height=3,command=lambda:press('-'))

button7 = Button(button_frame,text='7',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(7))

button8 = Button(button_frame,text='8',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(8))

button9 = Button(button_frame,text='9',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(9))

multiply = Button(button_frame,text='×',font=('times new roman',12),relief='ridge',
          bd=1,bg='#FF8C00',width=8,height=3,command=lambda:press('*'))

button0 = Button(button_frame,text='0',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press(0))

decimal = Button(button_frame,text='.',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=lambda:press('.'))

clear = Button(button_frame,text='C',font=('times new roman',12),relief='ridge',
          bd=1,bg='#808080',width=8,height=3,command=clear)

division = Button(button_frame,text='÷',font=('times new roman',12),relief='ridge',
          bd=1,bg='#FF8C00',width=8,height=3,command=lambda:press('÷'))

equal = Button(button_frame,text='=',font=('times new roman',12),relief='ridge',
          bd=1,bg='#FF8C00',width=35,height=3,command=equalpress)

expression_field.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=15)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
addition.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subtract.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
multiply.grid(row=3,column=3)

button0.grid(row=4,column=0)
decimal.grid(row=4,column=1)
clear.grid(row=4,column=2)
division.grid(row=4,column=3)

equal.grid(row=5,column=0,columnspan=4)

window.mainloop()
