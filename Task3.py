#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('C:\\Users\\personal\\Downloads\\householdtask3.csv')


# In[3]:


data.head(10)


# In[5]:


#Scatter plot year against own
plt.scatter(data['year'],data['own'])

#Adding title to the plot
plt.title("Scatter Plot")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[6]:


#Line Chart
plt.plot(data['year'])
plt.plot(data['own'])
#Adding title to the plot
plt.title("Line Chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[7]:


#Bar Chart or bar plot
plt.bar(data['year'],data['own'])

#Adding title to the plot
plt.title("Bar Chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[8]:


#Histogram
plt.hist(data['income'])

plt.title("Histogram")

plt.show()


# In[ ]:




