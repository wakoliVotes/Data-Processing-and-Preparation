#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np
import pandas as pd

TitanicData = pd.read_csv('D:/github/Python/train.csv')

# To get varied display rows, specify the value using the n item, e.g., n=8, or n=10, or n=30

TitanicData.head(n=10)                        # Gives 10 rows of dataset


# In[34]:


# Getting information about the used dataset
TitanicData.info()


# In[35]:


# Getting descriptive statistics information about the used dataset
TitanicData.describe()


# In[42]:


# To check all columns including those with categorical data, we add the "include='all'" in the describe() function

TitanicData.describe(include='all')     # Gives descriptive statistics for all columns

# The below output gives the descriptive statistics will all columns include


# In[ ]:





# In[ ]:




