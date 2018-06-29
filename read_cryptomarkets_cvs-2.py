
# coding: utf-8

# # Read in Cryptomarkets.cvs into DF
# 
# ## and perform some cleanups

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


#read in crypto-markets.csv in pandas DF
df = pd.read_csv('Data/crypto-markets.csv')

print(df.head())


# In[16]:


#df_clean = df.drop(columns=['slug','symbol']) will nicht!


# In[10]:


#count frequency of each curreny to determine which currencys we can drop
df_grouped = df.groupby('name').size()
df_grouped


# In[18]:


df_ranked = df_grouped.rank()
df_ranked


# In[42]:




