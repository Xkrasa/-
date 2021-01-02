#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
k=0
a=0
b=0
c=0

while k<10000:
    n = random.random()*361
    if n >= 0 and n <= 10:
        a += 1
    elif n > 10 and n <= 120:
        b += 1
    else:
        c += 1
    k=k+1
print("您抽到了{}个一等奖，{}个二等奖，{}个三等奖".format(a,b,c))


# In[ ]:




