#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[6]:


from nltk.chat.util import Chat, reflections
reflections


# In[ ]:


pairs = [
    ['need help',['how can I help you?']]
    ['how are you',['I am good']]
    ['what ia a chatbot',['it is a python program to help humans out']]
    ['are you a human?',['No']]
    
]
chat = Chat(pairs, reflections)
chat.converse()


# In[ ]:





# In[ ]:




