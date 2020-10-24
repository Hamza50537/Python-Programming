#!/usr/bin/env python
# coding: utf-8

# # Series

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[6]:


print(labels)
print(my_data)
print(arr)
print(d)


# In[10]:


pd.Series(my_data)  #pd.Series(data,index)


# In[11]:


pd.Series(my_data,labels)


# In[12]:


pd.Series(d)


# In[15]:


ser1=pd.Series([1,2,3,4],['Pak','China','Turkey','USA'])


# In[16]:


ser1


# # Data Frames
# Data Frame is the bunch of series that share the same index

# In[29]:


from numpy.random import randn


# In[30]:


np.random.seed(101)


# In[31]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[32]:


df


# In[33]:


df['W']


# In[34]:


type(df['W'])


# In[35]:


type(df)


# In[36]:


df.W


# In[42]:


df[['W','X','Y']]


# In[54]:


df['new']=df['W']+df['X']


# In[55]:


df


# In[56]:


df.drop('new',axis=1,inplace=True) #axis=0 refers to row/index for colum drop we have axis=1


# In[57]:


df #it's showing the dropped column because we have not set the inplace=True for parmenently remove of row or column


# In[58]:


df.shape


# In[59]:


df


# In[60]:


#Rows


# In[61]:


df.loc['A']


# In[62]:


type(df.loc['A'])


# In[65]:


df.iloc[0] #0th row


# In[66]:


df.iloc[1] #1st Row


# In[68]:


df.loc['B','Y'] #in row B select Y column


# In[72]:


df.loc[['B','C'],['W','X']]


# In[78]:


outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
#hier_index=pd.MultiIndex.from_tuples(hier_index)


# In[79]:


outside


# In[80]:


inside


# In[81]:


hier_index


# In[82]:


hier_index=pd.MultiIndex.from_tuples(hier_index)


# In[83]:


hier_index


# In[85]:


df=pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[86]:


df


# In[87]:


df.loc['G1']


# In[88]:


df.loc['G1'].loc[1]


# In[89]:


df.index.names


# In[90]:


df.index.names=['Groups','Num']


# In[91]:


df


# In[93]:


df.xs(1,level='Num') #want to get the values from multilevel


# # Group By
# The group By method allows you to group rows of data together and call aggregate functions

# In[94]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}


# In[95]:


df=pd.DataFrame(data)


# In[96]:


df


# In[97]:


byComp=df.groupby('Company')


# In[99]:


byComp.mean() #it performs the operation only on the colum with numbers we can't perfrom mean operation on strings


# In[100]:


byComp.sum()


# In[101]:


df.groupby('Company').describe()


# In[103]:


df.groupby('Company').describe().transpose()


# In[ ]:




