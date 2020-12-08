#!/usr/bin/env python
# coding: utf-8

# In[3]:


class BMI:
    def __init__(self,xingming,nianling,tizhong,shengao):
        self.xingming = xingming
        self.nianling = nianling
        self.tizhong = tizhong
        self.shengao = shengao
        self.bmi = tizhong/(shengao*shengao)
        t = self.bmi
        if t < 18.5:
            n = "偏瘦"
        elif t >= 18.5 and t < 24:
            n = "正常"
        elif t >= 24 and t < 30:
            n = "偏胖"
        self.jiankang = n
    def the_BMI(self):
        print("{n}".format(n=self.xingming),"的BMI是：{n}".format(n=self.bmi),"他/她的健康状况是：{n}".format(n=self.jiankang))
    def the_age(self):
        print("{n}".format(n=self.xingming),"的年龄是：{n}".format(n=self.nianling)) 
    def the_weighht(self):
        print("{n}".format(n=self.xingming),"的体重是：{n}".format(n=self.tizhong)) 
    def the_high(self):
        print("{n}".format(n=self.xingming),"的身高是：{n}".format(n=self.shengao))   


# In[5]:


zhangsan = BMI("zhangsan", "20", 140,175)


# In[8]:


zhangsan.the_BMI()


# In[10]:


zhangsan.the_age()

