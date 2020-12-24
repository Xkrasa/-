
# coding: utf-8

# In[10]:


import random 
import tkinter as tk
number=random.randint(100,999)
num=0
maxnum=999
minnum=100
running=True
def go():
    right=tk.Label(win,text='',bg='lightblue')
    right.pack_forget()
    global num
    global maxnum
    global minnum
    global running
    guess=content.get()
    num +=1
    text='第%d次尝试'%(num)
    tk.Label(win,text=text,bg='lightblue').place(x=10,y=60)
    try:
        if int(guess)==number:
            tk.Label(win,text='你猜对了',width=20,bg='lightblue').place(x=10,y=80)
        elif int(guess)>number:
            tk.Label(win,text='你猜的太大了',width=20,bg='lightblue').place(x=10,y=80)
        elif int(guess)<number:
            tk.Label(win,text='你猜的太小了',width=20,bg='lightblue').place(x=10,y=80)
    except:
        tk.Label(win,text='请输入正确的整数哟~',width=20,bg='lightblue').place(x=10,y=80)
        print('请输入正确的整数哟~')
def reset():
    global number
    global num
    #print('#------------------新的一局猜数字游戏------------------------#')
    number=random.randint(100,999)
    num=0
    tk.Label(win,text='              ',bg='lightblue').place(x=10,y=60)
    tk.Label(win,text='         ',width=18,bg='lightblue').place(x=10,y=80)
    tk.Label(win,text='                  ',width=18,bg='lightblue').place(x=130,y=0)
def answer():
    global number
    tk.Label(win,text='正确答案是:%d'%(number),width=18,bg='lightblue').place(x=130,y=0)
    
win=tk.Tk(className='猜数字游戏^v^')
win.geometry('400x100')
win['background']='lightblue'
tk.Label(win,text='请输入100到999的整数：',bg='lightblue').place(x=0,y=30)
content=tk.Entry(win,width=30,bg='white',fg='red')
content.place(x=150,y=30)
button=tk.Button(win,text='确认答案',command=go)
button.place(x=230,y=55)
replay=tk.Button(win,text='开启新局',command=reset)
replay.place(x=150,y=55)
answer=tk.Button(win,text='公布答案',command=answer)
answer.place(x=310,y=55)


