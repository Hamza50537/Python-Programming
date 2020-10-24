#!/usr/bin/env python
# coding: utf-8

# # For Loop

# In[12]:


inp=[1,2,3,4]


# In[13]:


out=[]

for num in inp:
    out.append(num**2)


# In[14]:


out


# In[15]:


out=[num**3 for num in inp]


# In[11]:


out


# # Function
# 

# In[16]:


def square(num):
    return num**2


# In[17]:


test=square(3)


# In[18]:


print(test)


# # Map Functions

# In[19]:


inp=[1,2,3,4]


# In[20]:


map(square,inp)


# In[22]:


list(map(square,inp))


# # Lambda/Anonymous Expressions

# In[27]:


target=lambda num:num**2


# In[28]:


target(3)


# In[29]:


inp=[1,2,3,4]


# In[30]:


list(map(lambda num:num**2,inp))


# # Filter Functions
# 
# It's the same as map but insted of mapping every element we will filter out the element and than apply the process

# In[35]:


list(filter(lambda num:num%2!=0, inp))


# # Built-in Methods for Strings

# In[49]:


test='abcdef jdjd kdsjks'


# In[50]:


test.upper()


# In[51]:


test.lower()


# In[52]:


test.split()


# In[53]:


test2='abcd!efgh'


# In[54]:


test2.split('!')


# In[55]:


test2.split('!')[1]


# # Built-in Functions for Dictionaries

# In[63]:


d={'k1':1,'k2':2}


# In[65]:


d['k1']


# In[66]:


d.keys()


# In[67]:


d.items()


# In[68]:


d.values()


# # Built-in Functions for Lists

# In[71]:


ls=[1,2,3,4]


# In[72]:


ls.pop()


# In[73]:


ls


# In[74]:


1 in ls


# Tuple and list

# In[75]:


x=[(1,2),(3,4),(5,6)]


# In[76]:


x[0]


# In[77]:


for item in x:
    print(item)


# In[78]:


for (a,b) in x:
    print(a)


# In[79]:


for (a,b) in x:
    print(b)


# In[80]:


for (a,b) in x:
    print(a)
    print(b)

