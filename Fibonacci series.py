#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)


n=int(input("enter a no."))
for a in range(1,n+1):
    print(fib(a),end=",")


# In[ ]:




