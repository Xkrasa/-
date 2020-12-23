#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random
import math
import tkinter.messagebox

root= tk.Tk() #创建页面
root.minsize(350,260)
root.title('猜数字游戏')#给程序窗口命名

number=random.randint(1,50) #随机生成数字


def guessnum():
    i = 1
    try:
        guess=text_guess.get()
        guess=int(guess)
        if guess == number and i <=5:
            tkinter.messagebox.showinfo("yes","恭喜猜对了!")
            i += 1 
        elif guess>number and i <= 5:
            tkinter.messagebox.showinfo("no","猜高了")
            i += 1
        elif guess < number and i <= 5:
            tkinter.messagebox.showinfo("no","猜低了")
            i += 1
        elif n>5:
            tkinter.messagebox.showinfo("game over","次数到了")
        elif guess != int
        label=tkinter.Label(root,text="欢迎加入游戏!")
        label.pack()
	except ValueError:
        tkinter.messagebox.showerror(title='Error', message='请输入数字')

#input 
label_guess=tkinter.Label(root,text='请输入猜的数字:')
label_guess.place(x=125,y=80)
text_guess=tkinter.Entry(root,width=10)
text_guess.place(x=132,y=150)
btnCheck=tkinter.Button(root,text='Guess',command=guessnum)
btnCheck.place(x=145,y=180,width=45,height=28)
 
root.mainloop()

