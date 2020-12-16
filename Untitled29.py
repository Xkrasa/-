#!/usr/bin/env python
# coding: utf-8

# In[51]:


import tkinter as tk
import random
import math
import tkinter.messagebox

root= tk.Tk() #创建页面
root.minsize(350,260)
root.title('猜数字游戏')#给程序窗口命名

number=random.randint(1,50) #随机生成数字


def guessnum():
    guess=text_guess.get()
    guess=int(guess)
    if guess>number:
        tkinter.messagebox.showinfo("no","猜高了")
    if guess < number:
        tkinter.messagebox.showinfo("no","猜低了")
    if guess == number:
        tkinter.messagebox.showinfo("yes","恭喜猜对了!")

def btn_confirm():
    myName=text_name.get()
    tkinter.messagebox.showinfo("name",'Well,'+myName+',I am thinking of a number between 1 and 20.')

label=tkinter.Label(root,text="欢迎加入游戏!")
label.pack()

#input 
label_guess=tkinter.Label(root,text='请输入猜的数字:')
label_guess.place(x=125,y=80)
text_guess=tkinter.Entry(root,width=10)
text_guess.place(x=132,y=150)
btnCheck=tkinter.Button(root,text='Guess',command=guessnum)
btnCheck.place(x=145,y=180,width=45,height=28)
 
root.mainloop()


# In[ ]:





# In[ ]:




