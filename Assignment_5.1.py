
# coding: utf-8

# In[22]:


(x,y) = (5,0)
try:
    z = x/y
except ZeroDivisionError:
    print("divide by zero")

