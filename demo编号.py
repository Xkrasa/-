#!/usr/bin/env python
# coding: utf-8

# In[ ]:


filename = ('E:/demo/demo.py')
with open(filename,'r')as fp:#赋值到fp上
    lines = fp.readlines()
maxLength = len(max(lines,key=len))# 找到最大长度
#传入命名参数key，其为一个函数，用来指定取最大值的方法（灵活运用，根据字典的键值）
line = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n'
       for index,line in enumerate(lines)]                 #开始编号
with open(filename[:-3]+'_new.py','w')as fp:
    fp.writelines(lines)

