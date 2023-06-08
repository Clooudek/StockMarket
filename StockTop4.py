#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


path = 'C:/Users/Klaud/Desktop/Project/individual_stocks_5yr'
company_list = ['AAPL_data.csv', 'GOOG_data.csv', 'MSFT_data.csv', 'AMZN_data.csv']
all_data=pd.DataFrame()
for file in company_list:
    current_df=pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data,current_df])
all_data.shape


# In[5]:


all_data.head


# In[12]:


all_data['date']=pd.to_datetime(all_data['date'])


# In[7]:


tech_list=all_data['Name'].unique()


# In[8]:


tech_list


# In[10]:


plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)
    
    


# In[13]:


import plotly.express as px


# In[14]:


for company in tech_list:
    df=all_data[all_data['Name']==company]
    fig=px.line(df,x='date',y='volume',title=company)
    fig.show()


# In[16]:


df=pd.read_csv('C:/Users/Klaud/Desktop/Project/individual_stocks_5yr/AAPL_data.csv')


# In[18]:


df.head()


# In[22]:


df['Daily_price_change']=df['close']-df['open']


# In[23]:


df.head()


# In[24]:


df['1day % return']=((df['close']-df['open'])/df['close'])*100


# In[25]:


df.head()


# In[26]:


fig=px.line(df,x='date',y='1day % return',title=company)
fig.show()


# In[27]:


df2=df.copy()


# In[28]:


df2.dtypes


# In[29]:


df2['date']=pd.to_datetime(df2['date'])


# In[30]:


df2.set_index('date', inplace=True)


# In[31]:


df2.head()


# In[32]:


df2['2013-02-08':'2013-02-14']


# In[34]:


df2['close'].resample('M').mean().plot()


# In[36]:


df2['close'].resample('Y').mean().plot(kind='bar')


# In[37]:


aapl=pd.read_csv('C:/Users/Klaud/Desktop/Project/individual_stocks_5yr/AAPL_data.csv')


# In[38]:


aapl.head()


# In[39]:


amzn=pd.read_csv('C:/Users/Klaud/Desktop/Project/individual_stocks_5yr/AMZN_data.csv')
amzn.head()


# In[42]:


msft=pd.read_csv('C:/Users/Klaud/Desktop/Project/individual_stocks_5yr/MSFT_data.csv')


# In[43]:


msft.head()


# In[44]:


goog=pd.read_csv('C:/Users/Klaud/Desktop/Project/individual_stocks_5yr/GOOG_data.csv')


# In[45]:


goog.head()


# In[46]:


close=pd.DataFrame()


# In[47]:


close['aapl']=aapl['close']
close['amzn']=amzn['close']
close['msft']=msft['close']
close['goog']=goog['close']


# In[49]:


close.head()


# In[50]:


import seaborn as sns


# In[51]:


sns.pairplot(data=close)


# In[52]:


sns.heatmap(close.corr(), annot=True)


# In[53]:


data=pd.DataFrame()


# In[54]:


data['aapl_change']=((aapl['close']-aapl['open'])/aapl['close'])*100
data['msft_change']=((msft['close']-msft['open'])/msft['close'])*100
data['goog_change']=((goog['close']-goog['open'])/goog['close'])*100
data['amzn_change']=((amzn['close']-amzn['open'])/amzn['close'])*100


# In[55]:


data.head()


# In[56]:


sns.pairplot(data=data)


# In[58]:


sns.heatmap(data.corr(),annot=True)


# In[59]:


sns.distplot(data['aapl_change'])


# In[60]:


data['aapl_change'].std()


# In[61]:


data['aapl_change'].std()*2


# In[62]:


data['aapl_change'].std()*3


# In[63]:


data['aapl_change'].quantile(0.1)


# In[65]:


data.describe().T


# In[ ]:




