#!/usr/bin/env python
# coding: utf-8

# In[3]:


text = ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']


# In[8]:


for i in text:
    print(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2))


# In[10]:


for i in text:
    print(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2)))


# In[14]:


l=[]
for i in text:
    l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2)))


# In[15]:


''.join(l)


# In[17]:


''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2)) for i in text])


# In[18]:


[i for i in range(10) if i%2==0]


# In[20]:


[ f'{i} X {j} = {i*j}' for i in range(2,10) for j in range(1,10)]


# In[21]:


'011011011'.replace('0','!').replace('!','+').replace('+','~')


# In[23]:


'1111'.zfill(10)


# In[28]:


s = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]


# In[29]:


s


# In[33]:


''.join(list(map(lambda x : chr(int(x,2)),s)))


# In[34]:


def f(x):
    return chr(int(x,2))

''.join(list(map(f,s)))

