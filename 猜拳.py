#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

import sys

print("欢迎来到猜拳小游戏")
while True:
    stats = input("欢迎“%s”来到本游戏，开始游戏输入Y，退出游戏输入N，请您输入：" % name)
    if stats == "Y" or stats == "y":
        print("游戏开始……")
        print("石头输入0、剪刀输入1、布输入2")
        break
    elif stats == "N" or stats == "n":
        print("游戏结束……")
        sys.exit(0)
    else:
        print("请按照要求重新输入！")
print("-------------加载中-------------")

def Game(user, comp):
    if (user== 0 and comp== 1) or (user== 1 and comp== 2) or (user== 2 and comp== 0):
        print("机器输入%d，您赢了！" % comp)
    elif user == comp:
        print("机器输入%d，平局了！" % comp)
    else:
        print("机器输入%d，您输了！" % comp)
    res = input("重新游戏请输入X，退出游戏按任意键")
    if res == "X" or res == "x":
        return
    else:
        sys.exit(0)
        
while True:
    user = int(input("请您出拳，输入相应数字！"))
    if user == 0 or user == 1 or user == 2:
        comp = random.randint(0, 2)
        Game(user, comp)
    else:
        print("输入数字有误，请确认后，重新输入！")

