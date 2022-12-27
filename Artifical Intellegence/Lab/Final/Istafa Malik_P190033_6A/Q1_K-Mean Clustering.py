#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import random


# In[15]:


df = pd.read_csv("wine.data", delimiter = '\t')


# In[16]:


df.head()


# In[18]:


x = np.array(df)
random.shuffle(x)
k = 4    


# In[19]:


centroids_index = np.random.randint(0, 58,( 4,))
centroids_index


# In[20]:


x[centroids_index]


# In[21]:


ctds = x[centroids_index]


# In[22]:


ctds


# In[23]:


x= np.delete(x,centroids_index, axis = 0)


# In[24]:


clusters = [[], [], [], []]
clusters[0].append(ctds[0])
clusters[1].append(ctds[1])
clusters[2].append(ctds[2])
clusters[3].append(ctds[3])


# In[25]:


def euclidean_distance(centroid, x):
    difference = np.array(x) - np.array(centroid)
    sqrd_diff = np.square(difference)
    sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
    distance = np.sqrt(sum_sqrd_diff)
    
    return distance


# In[26]:


clusters


# In[27]:


len(clusters[0])


# In[28]:


len(clusters[1])


# In[29]:


len(clusters[2])


# In[30]:


len(clusters[3])


# In[31]:


c1 = euclidean_distance(ctds[0], x)
c2 = euclidean_distance(ctds[1], x)
c3 = euclidean_distance(ctds[2], x)
c4 = euclidean_distance(ctds[3], x)


# In[32]:


c1


# In[33]:


ctds[0]


# In[34]:


len(x)


# In[35]:


len(c1)


# In[36]:


for i in x:
    id = np.argmin(euclidean_distance(i, ctds))
    clusters[id].append(i)


# In[37]:


clusters


# In[38]:


ctds[0] = np.mean(clusters[0], axis = 0)
ctds[1] = np.mean(clusters[1], axis = 0)
ctds[2] = np.mean(clusters[2], axis = 0)
ctds[3] = np.mean(clusters[3], axis = 0)


# In[39]:


for i in range(1):
    prev_clusters = clusters
    
    prev_centroids = [ctds[0], ctds[1], ctds[2], ctds[3]]
    c1 = euclidean_distance(ctds[0], x)
    c2 = euclidean_distance(ctds[1], x)
    c3 = euclidean_distance(ctds[2], x)
    c4 = euclidean_distance(ctds[3], x)
    
    clusters = [[], [], [], []]
    clusters[0].append(ctds[0])
    clusters[1].append(ctds[1])
    clusters[2].append(ctds[2])
    clusters[3].append(ctds[3])
    
    for j in x:

        id = np.argmin(euclidean_distance(j, ctds))
        clusters[id].append(j)
    
    ctds[0] = np.mean(clusters[0], axis = 0)
    ctds[1] = np.mean(clusters[1], axis = 0)
    ctds[2] = np.mean(clusters[2], axis = 0)
    ctds[3] = np.mean(clusters[3], axis = 0)
    
    new_centroids = [ctds[0], ctds[1], ctds[2], ctds[3]]
    
    if np.array_equiv( prev_centroids, new_centroids):
        print("Centroids of newly formed clusters do not change.")
        break
    
    if np.array_equiv(prev_clusters, clusters):
        print("Points remain in the same cluster.")
        break
        
    
clusters


# In[40]:


len(clusters[0])


# In[41]:


len(clusters[1])


# In[42]:


len(clusters[2])


# In[43]:


len(clusters[3])


# In[44]:


total = len(clusters[0]) + len(clusters[1]) + len(clusters[2]) + len(clusters[3])
total


# In[ ]:





# In[ ]:




