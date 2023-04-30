#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#using pandas to read the database stored in the same folder
data=pd.read_csv('mnist.csv')


# In[3]:


#viewing column heads
data.head()


# In[4]:


#extracting data from dataset and viewing them up close
a=data.iloc[3,1:].values


# In[6]:


#reshaping the extracted data into a resonable size
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[7]:


#preparing the data
#separating labels and data values
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]


# In[8]:


#creating test and train sizes/batches
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)


# In[9]:


#check data
y_train.head()


# In[10]:


#call rf classifier
rf= RandomForestClassifier(n_estimators=100)


# In[12]:


#fit the model
rf.fit(x_train,y_train)


# In[13]:


#prediction on test data
pred= rf.predict(x_test)


# In[14]:


pred


# In[15]:


#check prediction accuracy
s=y_test.values

#calculate number of correctly predicted values
count=0
for i in range (len(pred)):
    if pred[i]==s[i]:
        count=count+1


# In[16]:


count


# In[17]:


#total values that the prediction code was run on
len(pred)


# In[18]:


#accuracy value
8096/8400


# In[ ]:




