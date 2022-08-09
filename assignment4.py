#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy


# In[9]:


df=pd.read_excel('F:\cleantechsolar/assignment.xlsx')


# In[10]:


df


# In[6]:


df.head()


# In[7]:


df.info()


# In[ ]:





# In[8]:


sns.scatterplot(data =df ,x = 'Date', y ='PR', hue ='GHI')


# In[9]:


df['GHI'].value_counts()


# In[10]:


df['PR'].value_counts()


# In[11]:


df['Date'].value_counts()


# In[37]:



perpr = ((np.asarray(df['PR'])).reshape(982,1))
perghi = ((np.asarray(df['GHI'])).reshape(982,1))
print(perpr)
print(perghi)


# In[52]:





# In[43]:


(df.groupby('PR').Date.value_counts().unstack())


# In[44]:


solar_data=(df.groupby('PR').Date.value_counts().unstack())


# In[45]:


sns.heatmap(solar_data);


# In[46]:


(df.groupby('GHI').Date.value_counts().unstack())


# In[47]:


solar_data=(df.groupby('GHI').Date.value_counts().unstack())


# In[48]:


sns.heatmap(solar_data);


# In[ ]:




