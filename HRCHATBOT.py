#!/usr/bin/env python
# coding: utf-8

# In[22]:


import nltk
import re
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
df=pd.read_excel("C:\\Users\Pankaj\Desktop\ChatBot\hr_excelnew.xlsx")


# In[23]:


df.head()


# In[24]:


df.isnull().sum()


# In[25]:


df.shape


# In[26]:


df['Category'].value_counts()


# In[27]:


df_new=df.copy()


# In[28]:


def textcleaning(text):
    text=re.sub('#\S+', '', text)  # remove hashtags
    text=re.sub('@\S+', '  ', text)  # remove mentions
    text=re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text=text.encode('ascii','ignore')
    text=text.decode()
    text=re.sub('\S*\d+\S*',' ',text)
    text=re.sub('\s+', ' ', text)# remove extra whitespace
    text=text.lower()
    return text


# In[29]:


for i in range(len(df_new)):
    df_new['Message'][i]=textcleaning(df_new['Message'][i])
df_new.head()


# In[30]:


#label_enc=LabelEncoder()
#df_new['Category']=label_enc.fit_transform(df_new['Category'])


# In[31]:


StopWords = set(stopwords.words('english'))
stemmer=PorterStemmer()


# In[32]:


def textstemming(text):
    words=text.split()
    words=[stemmer.stem(word) for word in words if word not in StopWords]
    text=' '.join(words)
    return text


# In[33]:


for i in range(len(df_new)):
    df_new['Message'][i]=textstemming(df_new['Message'][i])
df_new.head()


# In[34]:


from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(df_new['Message'])
Y=df_new['Category']


# In[35]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=5, test_size=0.2)
from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(X_train,Y_train)
predictions=clf.predict(X_test)








# In[ ]:




