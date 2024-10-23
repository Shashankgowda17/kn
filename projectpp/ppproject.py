#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\Shash\OneDrive\Documents\1. Weather Data.csv")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data['Weather'].unique()


# In[12]:


data.nunique()


# In[13]:


data.count()


# In[14]:


data['Weather'].value_counts()


# In[15]:


data.info()


# In[16]:


data.head()


# In[17]:


data.nunique()


# In[18]:


data['Wind Speed_km/h'].nunique()


# In[19]:


#no of times'weather is exactly clear'.
data.head(2)
data.Weather.value_counts()


# In[20]:


#filetering
data.head(2)
data[data.Weather == 'clear']


# In[44]:


data.groupby('Weather').get_group('Clear')


# In[22]:


#wind speed exactly 4 times
data[data['Wind Speed_km/h'] ==4]


# In[23]:


#find null values
data.isnull().sum()


# In[25]:


data.notnull().sum()


# In[47]:


#rename 'weather'to'weathercondntion'.
data.rename(columns ={'Weather':'Weather Condition'})


# In[27]:


#mean value of visiblity.
data.Visibility_km.mean()


# In[29]:


#variance of humidity.
data['Rel Hum_%'].var()


# In[36]:


#'snow'was recorded.
data['Weather'].value_counts()


# In[45]:


data[data['Weather'] =='snow']


# In[50]:


#str.contains
data[data['Weather'].str.contains('snow')]


# In[52]:


data.groupby('Weather').mean()


# In[53]:


#minimum & maximum
data.groupby('Weather').min()


# In[54]:


data.groupby('Weather').max()


# In[57]:


#fog
data[data['Weather'] == 'Fog']


# In[60]:


#"weather is clear"or "visiblity above"40
data[(data['Weather'] == 'clear') | (data['Visibility_km'] > 40)]


# In[62]:


#weather is clear & relative humidity>50.
data[(data['Weather'] == 'clear') & (data['Rel Hum_%']>50)|(data['Visibility_km']>40)]


# In[ ]:




