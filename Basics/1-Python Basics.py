#!/usr/bin/env python
# coding: utf-8

# # String

# In[ ]:


num=12
name='sam'


# In[2]:


'My number is {} and my name is {}'.format(num,name)


# In[3]:


print('My number is {} and my name is {}'.format(num,name))


# Here in this format it does not depend what sequence you use in format but inside the curly brackets it still matters

# In[6]:


print('My number is {one} and my name is {two}'.format(two=name,one=num))


# ## Indexing Strings

# In[7]:


s='hello'


# In[11]:


s[0:]


# In[12]:


s[:3]


# In[14]:


s[1:3]


# # List

# In[20]:


numbers_List=[1,2,3]


# In[21]:


print(numbers_List)


# In[22]:


strings_List=['a','b','c']


# In[24]:


print(strings_List)


# In[25]:


strings_List.append('d')


# In[26]:


strings_List


# In[28]:


strings_List[1:3]


# ## Nesting Lists

# In[30]:


demo=[1,2,[3,4]]


# In[31]:


demo


# In[32]:


demo[2]


# In[34]:


demo[2][0]


# In[35]:


demo[2][0]


# In[47]:


nested_Lists=[1,2,3,[4,5,['test','done']]]


# In[48]:


nested_Lists


# In[49]:


nested_Lists[0:3]


# In[50]:


nested_Lists[3]


# In[51]:


nested_Lists[3][0]


# In[52]:


nested_Lists[3][1]


# In[53]:


nested_Lists[3][2][0]


# In[54]:


nested_Lists[3][2][1]


# # Dictionaries

# Dictionaries behave as a key value pair just like a hash table and instead of holding the elements through sequence they hold the elements using keys and values pairs
# 
# Dictionaries can take any item.
# 

# In[57]:


dict1={'key1':'value','key2':456}


# In[60]:


dict1['key1']


# In[61]:


dict1['key2']


# In[62]:


dict2={'key1':[1,2,3],'key2':'abcd','key3':123}


# In[63]:


dict2['key1']


# In[69]:


dict2['key1'][0]


# In[70]:


dict2['key2']


# In[71]:


dict2['key3']


# In[72]:


dict3={'k1':{'innerkey':[1,2,3]}}


# In[73]:


dict3['k1']


# In[74]:


dict3['k1']['innerkey']


# In[75]:


dict3['k1']['innerkey'][0]


# # Tuples
# 1-Tuple is the same as list except that you define it using ().(Note: List uses [])
# 2-Tuple is immutable means that you cannot change the values inside the tuple but in lists we can do that thing.

# In[78]:


t=(1,2,3)


# In[79]:


t[0]


# # Sets
# 1-Set is the collection of unique elements

# In[80]:


set1={1,2,3}


# In[81]:


set1


# In[82]:


set([1,2,2,3,3,3,4,4])


# In[85]:


set1.add(4)


# In[87]:


set1

