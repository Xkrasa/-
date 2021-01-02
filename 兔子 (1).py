#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

f = 0

def set_1():
    global cave,time_num,initial,cnum,f,ch
    try:
        print("请输入洞的数量：")
        cnum = int(input())
        if cnum <= 2:
            print("太少了，请设置足够的数量！")
            set_1()
    except ValueError:
        print("请输入正确格式的整数")
        set_1()
        
def set_2():
    global cave,time_num,initial,cnum,f,ch
    try:
        print("请输入抓兔子的次数上限：")
        time_num = int(input())
        cave = [0] * cnum
        initial = random.randint(1,cnum)
        cave[initial-1] = 1
        f = 0
        if time_num < 1:
            print("太少了，请设置足够的数量！")
            set_2()
    except ValueError:
        print("请输入正确格式的整数")
        set_2()
        
def jump(x):
    global cave,time_num,initial,cnum,f,ch
    if x != 0 and x != cnum:
        if random.randint(0, 1) == 0:
            x -= 1
        else:
            x += 1
    elif x == cnum:
        if random.randint(0, 1) == 0:
            x -=1
        else:
            x =0
    else:
        if random.randint(0, 1) == 0:
            x += 1
        else:
            x = cnum
    return x

def catchme():
    global cave,time_num,initial,cnum,f,ch
    if f == 0:
        set_1()
        set_2()
    while time_num != 0:
        print("这次抓哪个洞：")
        try:
            ca = int(input()) - 1
            if cave[ca] == 1:
                print("恭喜你抓到了")
                f = 0
                break
            elif f == 0:
                cave[initial - 1] = 0
                ch = jump(initial)
                cave[ch] = 1
                time_num -= 1
                print("未抓到，你还剩%d次机会"%time_num)
                f = 1
            else:
                cave[ch - 1] = 0
                ch = jump(ch)
                cave[ch] = 1
                time_num -= 1
                if time_num == 0:
                    print("次数用完了")
                    f = 0
                    break
                else:
                    print("未抓到，你还剩%d次机会"%time_num)
        except ValueError:
            print('你输入的不是数字哦')
        except IndexError:
            print('请输入范围内的数')
        except:
            print('请输入完整的条件')

catchme()


# ### 
