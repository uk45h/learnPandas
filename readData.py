#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
broken_df = pd.read_csv('sample-data/csv/userdata1.csv')
broken_df[:3]



# In[20]:


fixed_df = pd.read_csv('sample-data/csv/userdata1.csv', sep=',', encoding='latin1',parse_dates=['registration_dttm'], dayfirst=True, index_col='id')
fixed_df[:3]


# In[36]:


fixed_df['hour'] = fixed_df['registration_dttm'].dt.hour
fixed_df[['registration_dttm','hour']].head(10)


# In[39]:


fixed_df[['salary','hour']].plot.scatter(x="salary",y='hour')


# In[41]:


#need dependency 'pyarrow' or/and dependency 'fastparquet'
par=pd.read_parquet('sample-data/parquet/userdata1.parquet', engine='pyarrow')
par[:3]


# In[ ]:




