#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


df = pd.read_csv('jabar.csv')


# In[7]:


df.head(7)


# In[8]:


r = 0.43


# In[9]:


import math
pi=math.pi


# In[10]:


C = 2*pi*r 


# In[11]:


A = pi*r*r


# In[12]:


print("Circumference: " + str(C))


# In[13]:


print("Area: " + str(A))


# In[ ]:




