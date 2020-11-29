#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'walden.py', '#打开并读取文件\nfile = open(r\'C:\\Users\\Administrator\\Desktop\\Walden.txt\',\'r\')\nlines = file.readlines() \n# 要把每行拆成单词\nwords = []\n\nfor line in lines:\n    tmp_list = line.split(" ")\n    for word in tmp_list:\n        words.append(word.replace(\',\',\'\').replace(\'.\',\'\').replace(\':\',\'\').replace(\';\',\'\').lower())\n#对word中每一个元素计算他出现的个数\n#把统计结果保存到字典中，字典的key是单词，value是单词出现的次数\nword_count = {}\nword_set = set(words)\nfor word in words:\n    count_num = words.count(word)\n    word_count[word] = count_num\n\nword_count\n#对word_count字典进行排序，按照出现的次数（value）降序排序\nsorted(word_count.items(),key=lambda item: item[1],reverse=True)\n\n#word_count.items\n\n\n  ')


# In[ ]:




