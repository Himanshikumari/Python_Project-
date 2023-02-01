#!/usr/bin/env python
# coding: utf-8

# <img src="https://www.usnews.com/dims4/USNEWS/6d9d1e5/2147483647/thumbnail/970x647/quality/85/?url=https%3A%2F%2Fwww.usnews.com%2Fcmsmedia%2F38%2Fe6%2F58c88e3c4d2e9dd1a7055521da7f%2F201016-udemy-stock.png"/>

# # Data Analysis project
# ## Udemy Courses dataset
# #### This data is taken from the internet. And this is a clean data.
# #### By Himanshi Kumari

# ### step 1:install Libraries

# In[2]:


import pandas as pd


# ### step 2: Load the data

# In[3]:


data=pd.read_csv(r"C:\Users\Himanshi\Desktop\udemy\Udemy_Courses.csv")


# In[4]:


data


# ### To see top 5 records we use head command

# In[5]:


data.head()


# ### To see last 5 records we use tail command

# In[6]:


data.tail()


# ### describe the data 

# In[7]:


data.describe()


# ### gives information about the data whether null values are presnet or not

# In[8]:


data.info()


# ### to know whether null values are present in data or not

# In[10]:


data.isnull()


# ### size() function count the number of elements along a given axis

# In[12]:


data.size


# ### ndim() function return the number of dimensions of an array

# In[13]:


data.ndim


# ### count() method returns the number of elements with the specified value i.e axis=0 is used for row and axis=1 is used for column.

# In[14]:


data.count(axis=0) #0 is used for row


# ### count() method returns the number of elements with the specified value

# In[15]:


data.count(axis=1)


# In[ ]:





# In[ ]:





# ### 1.What are all different subjects for which Udemy is offering courses ?

# In[16]:


data.subject.unique()


# ### 2.Which subject has the maximum number of courses.

# In[22]:


data.subject.value_counts()


# In[24]:


max(data.subject[data.subject.value_counts()])


# In[25]:


max(data.subject.value_counts())


# In[ ]:





# ### 3.Show all the courses which are Free of Cost.

# In[26]:


data.head(1)


# In[32]:


data[data.is_paid == False]


# ### 4. Show all the courses which are Paid.

# In[35]:


data[data.is_paid== True]


# ###  5.Which are Top Selling Courses ?

# In[36]:


data.head(1)


# In[46]:


data.sort_values('num_subscribers', ascending=False)


# ### 6. Which are Least Selling Courses ?

# In[54]:


data.sort_values('num_subscribers', ascending=True)


# ### 7. Show all courses of Graphic Design where the price is below 100 ?

# In[55]:


data.head(1)


# In[66]:


data[(data.subject == "Graphic Design") & (data.price >'100')]


# In[70]:


data[(data.subject == "Graphic Design") & (data.price <'100')]


# ### 8. List out all the courses that are related to 'Python'.

# In[71]:


data.head(1)


# In[73]:


data[data.course_title.str.contains("Python")]


# ### 9.What are courses that were published in the year 2015 ?

# In[77]:


data.published_timestamp=pd.to_datetime(data.published_timestamp) #publish timestamp column is in obejct data type to work with it we have to change it into datetime format.


# In[78]:


data.dtypes


# ### to separate the year from publish timestamp column

# In[79]:


data['year']=data.published_timestamp.dt.year


# In[80]:


data.head(1)


# In[81]:


data[data.year==2015]


# ### 10.What is the Max. Number of Subscribers for Each Level of courses ?

# In[84]:


data.level.unique()


# In[86]:


data.groupby('level')['num_subscribers'].max()


# In[ ]:





# In[88]:


import matplotlib.pyplot as plt
import numpy as np


# In[90]:


x = data.course_title
y = data.num_subscribers

plt.bar(x,y)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




