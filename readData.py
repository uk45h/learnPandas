#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[19]:


#need dependency 'pyarrow' or/and dependency 'fastparquet'
par1=pd.read_parquet('sample-data/parquet/userdata1.parquet', engine='fastparquet', index='id')
par[:3]


# In[18]:


par=pd.read_parquet('sample-data/parquet', engine='fastparquet')
par[:3]


# In[3]:


from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())


# In[20]:


q = """SELECT count(*) 
       FROM par1 ;"""

names = pysqldf(q)
names.head(5)


# In[21]:


q = """SELECT count(*) 
       FROM par ;"""

names = pysqldf(q)
names.head(5)


# In[22]:


par.to_csv('sample-data/parquet_to_csv.csv')


# In[ ]:




