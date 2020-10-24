#!/usr/bin/env python
# coding: utf-8

# # Numpy Arrays

# In[1]:


import numpy as np


# In[3]:


my_List=[1,2,3,4]


# In[5]:


arr=np.array(my_List)


# In[6]:


arr


# In[7]:


my_Lists=[[1,2,3],[4,5,6],[7,8,9]]


# In[8]:


arr1=np.array(my_Lists)


# In[9]:


arr1


# In[10]:


arr1[0]


# In[11]:


arr1[0][0]


# In[12]:


arr1[0][1]


# In[14]:


np.arange(1,10)  #np.arrange(start,end,step)


# In[15]:


np.arange(1,10,2)


# In[16]:


np.zeros(3)


# In[18]:


np.zeros((3,3))


# In[19]:


np.ones(4)


# In[20]:


np.ones((4,4))


# In[23]:


np.ones((2,2,3))


# In[25]:


np.eye(4) #identitiy Matrix


# In[27]:


np.random.rand(3,3)  #Returns Numbers from Uniform Number Distribution between 0 to 1


# In[28]:


np.random.randn(2) #Returns Numbers from Standard Number Distribution between 0 to 1


# In[30]:


np.random.randn(3,3)


# In[31]:


np.random.randint(1,100)


# In[32]:


np.random.randint(1,100,10)


# In[34]:


arr=np.arange(25)


# In[35]:


arr


# In[36]:


randr=np.random.randint(1,10,20)


# In[37]:


randr


# In[38]:


arr.reshape(5,5)


# In[39]:


randr.max()


# In[40]:


randr.min()


# In[42]:


randr.argmax()


# In[44]:


arr1=np.arange(0,11)


# In[45]:


arr1


# In[47]:


arr1[0:5]


# In[49]:


arr1[5:]


# In[51]:


slice_of_arr1=arr1[0:4]


# In[52]:


slice_of_arr1[:]=99


# In[53]:


slice_of_arr1


# In[54]:


arr1


# # 2d Array

# In[55]:


array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[56]:


array_2d


# In[57]:


array_2d[0]


# In[58]:


array_2d[0][2]


# In[61]:


array_2d[1,0] #arr[row,col]


# In[64]:


array_2d[:1,:1,]


# In[66]:


array_2d[:2,:2,]


# In[67]:


arr=np.arange(0,10)


# In[68]:


arr


# In[69]:


bool_arr=arr>5


# In[70]:


bool_arr


# In[71]:


arr[bool_arr]


# In[85]:


arr_2d=np.arange(10).reshape(5,2)


# In[86]:


arr_2d


# In[87]:


arr_2d[1:3,]


# In[88]:


arr_2d[1:3,1:]

