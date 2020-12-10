
# coding: utf-8

# In[138]:


class BMI:
    #初始化
    def __init__(self, name, age, weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bmi = self.weight / (self.height * self.height)
        self.bmi = round(self.bmi, 2)
    def get_name(self):
        print(self.name)  #直接print
        return self.name # 返回值
    
    def get_bmi(self):
        
        return self.bmi
    
    def get_statues(self):
        if self.bmi < 18.5:
            self.status = "偏瘦"
        elif self.bmi >= 18.5 and self.bmi < 24:
            self.status = "正常"
        elif self.bmi >= 24 and self.bmi < 30:
            self.status = "偏胖"
        return self.status


# In[139]:


bmi1 = BMI("zhangsan", 18, 60, 1.7) # 实例化


# In[140]:


bmi1.get_statues()


# In[141]:


print("{n} 的BMI是：{b} ，身体状态是：{s} ".format(n = bmi1.get_name(),b = bmi1.get_bmi(),s = bmi1.get_statues()))

