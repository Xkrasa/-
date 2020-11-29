#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('writefile', 'chazhao.py', '#创建一个字典students,key是学号，value是姓名\n#学生信息在stdents.csv文件里，从文件中读取并保存到字典\n#打开student.csv文件\nfile = open(\'C:/Users/Administrator/Desktop/students.csv\',\'r\')  #也可以在地址前加一个字母 r\n#读取文件中的内容\nlines = file.readlines()\n# 抽取每行的学号和姓名，保存到字典\nstudents = {}\nfor line in lines:\n    tmp_list = line.split(\',\')\n    xuehao = tmp_list[0]\n    xingming = tmp_list[1]\n    students[xuehao] = xingming\n    \n#从学号中随机抽取学号\nimport random\n \nnum = int(input("输入随机抽取的人数："))\n#如何把字典中的key（学号）取成列表\n\nxuehao_list = random.sample(students.keys(),num)\nxuehao_list\n#根据随机抽取的学号，打印输入对应的学号\nfor xuehao in xuehao_list:\n    print(students[xuehao])')

