#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Queston 2
# Part A population

import random
best=-100000
populations =([[random.randint(1,5) for x in range(6)] for i in range(4)])
print(type(populations))
parents=[]
new_populations = []
print(populations)

# Part B fitness 

def fitness_score() :
    global populations,best
    fit_value = []
    fit_score=[]
    for i in range(4) :
        chromosome_value=5
        
        for j in range(5,0,-1) :
            chromosome_value += populations[i][j]*(2**(5-j))
        chromosome_value = -1*chromosome_value if populations[i][0]==1 else chromosome_value
        print(chromosome_value)
        fit_value.append(-(chromosome_value**2) + 5 )
    print(fit_value)
    fit_value, populations = zip(*sorted(zip(fit_value, populations) , reverse = True))
    best= fit_value[0]
    
fitness_score()

# Part C Mutation

def mutation() :
    global populations, parents
    mute = random.randint(0,49)
    if mute == 20 :
        x=random.randint(0,3)
        y = random.randint(0,5)
        parents[x][y] = 1-parents[x][y]
    populations = parents
    print(populations)


# In[ ]:




