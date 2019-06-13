#!/usr/bin/env python
# coding: utf-8

# # numpy套件

# In[1]:


a_list=[1,2,3,4,5]
print(a_list*3)


# In[3]:


#numpy套件ndrray型態，提供element-wise的操作
import numpy as np
a_ndarray=np.array([1,2,3,4,5])
print(a_ndarray*3)


# In[4]:


print(type(a_ndarray))
print(a_ndarray.ndim) #ndarray的維度
print(a_ndarray.shape) #ndarray的shape
print(a_ndarray.dtype) #ndarray的資料型態


# In[5]:


z=np.zeros(6)
print(z) #六個元素都為0的id ndarray
print(np.zeros((2,6))) #12個元素都為0的2d ndarray
print(np.empty((2,6,2))) #24個元素都未初始化的值
print(np.arange(10)) #10個元素維0-9的id ndarray


# # ndarray的進階操作

# In[6]:


my_array=np.arange(10)
print(my_array)
print(my_array[0])
print(my_array[0:5])


# In[7]:


#2維ndarray取值
my_2d_array = np.array([np.arange(0,5), np.arange(5,10)])
print(my_2d_array)
print(my_2d_array[1,:]) #第二列資料
print(my_2d_array[:,1]) #第二欄資料
print(my_2d_array[1:1]) #第二列第二欄的資料


# In[8]:


#2維ndarray取值
my_2d_array = np.array([np.arange(0,5), np.arange(5,10)])
#print(my_2d_array)
print(my_2d_array[1,:2]) #第二列資料 取2個
#print(my_2d_array[:,1]) #第二欄資料
#print(my_2d_array[1:1]) #第二列第二欄的資料


# In[9]:


#2維ndarray取值
my_2d_array = np.array([np.arange(0,5), np.arange(5,10)])
#print(my_2d_array)
print(my_2d_array[1,:-2]) #第二列資料 倒2個取
#print(my_2d_array[:,1]) #第二欄資料
#print(my_2d_array[1:1]) #第二列第二欄的資料


# In[17]:


#假設有六個組別"Modern Web", "DevOps", "Cloud", "Big", "Data", "Security", "自我挑戰組" 
#其參加人數分為56, 8, 19, 14, 6, 71人
groups=['Modern Web', 'DevOps', 'Cloud', 'BigData', 'Security', '自我挑戰組']
ironman = [56,8,19,14,6,71]
groups_array = np.array(groups)
ironman_array = np.array(ironman)
print(groups_array)
print(ironman_array)


# In[18]:


#用人數去篩選組別
print(ironman_array >= 10)
print(groups_array[ironman_array >= 10])
print(groups_array != "自我挑戰組")
print(ironman_array[groups_array != "自我挑戰組"])


# # Ndarray轉置

# In[19]:


my_1d_array=np.arange(10)
print(my_1d_array)
my_2d_array=my_1d_array.reshape((2,5))
print(my_2d_array)
print(my_2d_array.T)


# In[21]:


print(np.arange(24).reshape(4,6))


# In[22]:


#ndarray nan(空值)
nan_array=np.array([56,8,19,14,6, np.nan])
print(nan_array)


# In[ ]:




