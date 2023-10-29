#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import warnings
warnings.filterwarnings('ignore')


# In[7]:


#sample
text='This is a simple example:we are going to process this text,removing stopwords and punctation. we removed and done with processing'


# In[9]:


rint(string.punctuation)


# In[11]:


text="".join([i for i in text if i not in string.punctuation ])
text


# In[12]:


#lowering the text
text=text.lower()
text


# In[14]:


#tokenization
words=word_tokenize(text)
print(words)


# In[16]:


#stop words removal
nltk.download('stopwords')


# In[17]:


stop_words=set(stopwords.words("english"))
print(stop_words)
print (len(stop_words))


# In[22]:


#filtered words
filtered_words=[word for word in words if word not in stop_words]
print(filtered_words)


# In[23]:


#stemming

from nltk.stem.porter import PorterStemmer
porter_stemmer=PorterStemmer()


# In[24]:


stem_text=[porter_stemmer.stem(word) for word in filtered_words]
print(stem_text)


# In[ ]:




