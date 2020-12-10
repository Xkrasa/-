
# coding: utf-8

# In[5]:


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
# 标签
l = tk.Label(window,textvariable = var,bg = 'green',font = ('Arial',12),width = 15,height = 2) #参数
l.pack() #安置（方位）
on_hit = False
#按钮
def hit_me():
    global on_hit 
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
        
b = tk.Button(window,text = 'hit me',width = 15,
                height = 2,command = hit_me)
b.pack(side='bottom')
window.mainloop()

