#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([[8,9,20], [10,31,22]])
b = np.array([[1,2,3], [4,5,6]])
print(a-b)


# In[5]:


s=np.array([ [1,2,3], [4,5,6] ])

print(s.shape)


# In[6]:


import numpy as np
b = np.array([[1,2], [3,4]])
print(b.transpose())


# In[7]:


4
import numpy as np
b = np.array([[1,2], [3,4]])
print(np.sum (b, axis = 1))


# In[10]:


1
s = 'Sheher mein'
a = 'aeiouAEIOU'
for i in range(len(s)):

    if(s.index(s[i])%2 == 0): 
        print(i)

    if(s[i] in a):

        s = s.replace(s[i], '_')

print(s)


# In[11]:


123
s = 'The Joy of Computing'
print(s[3:12])


# In[15]:


1
2
a = ['', 'h', 'e', 'l','','l']
print('.'.join(a))


# In[17]:


s = 'Hello Everyone' 
print(s.lower())


# In[ ]:




