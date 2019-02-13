
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency #方差检验
import seaborn as sns
import copy 
import gc
get_ipython().magic('matplotlib inline')
plt.style.use("ggplot")


# In[2]:

def memory_optimze(df):
    print("**********正在统计数据所占内存大小****************")
    memory_0 = df.memory_usage(deep="True").sum()/1024.0/1024.0
    print("*******处理int型***************")
    for i in df.select_dtypes(include=["integer"]).columns:
        df[i] = pd.to_numeric(df[i],downcast="integer")
        
    print("******处理float型**************")
    for i in df.select_dtypes(include=["float"]).columns:
        df[i] = pd.to_numeric(df[i],downcast="float")
    print("**********处理object型（字符型）**************")
    
    for i in df.select_dtypes(include=["object"]).columns:

        df[i] = df[i].astype("category")

    if all(i in df.columns.tolist() for i in ["weekday","minute","month","date"]):
        delete_flag = input('是否要删除列名["weekday","minute","month","date"]:Y/N')
        if delete_flag =='Y':
            print('正在删除列["weekday","minute","month","date"]')
            df =df.drop(["weekday","minute","month","date"],axis=1)
            print("删除完毕!!")
        else:
            print("不删除！！")
    memory_1 = df.memory_usage(deep="True").sum()/1024.0/1024.0

    print("优化前，数据集所占内存大小为{0}M".format(memory_0))
    print("优化后，数据集所占内存大小为{0}M".format(memory_1))
    print("优化后，内存减小了{0}%".format((memory_0-memory_1)/memory_0 * 100))
    return df
    


# In[3]:



# In[4]:


# In[ ]:



