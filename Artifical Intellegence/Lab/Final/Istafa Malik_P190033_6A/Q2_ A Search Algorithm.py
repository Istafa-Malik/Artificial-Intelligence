#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")
import pprint
from queue import PriorityQueue


# In[4]:


def draw_graph_with_nx(G):


# In[5]:


pos = nx.spring_layout(G, iterations=200)
options = {'node_color': 'white', 'alpha': 1, 'node_size': 2000,
'width': 0.002, 'font_color': 'darkred',
'font_size': 25, 'arrows': True, 'edge_color': 'brown',
'arrowstyle': 'Fancy, head_length=1, head_width=1,
tail_width=.4'
}


# In[6]:


labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, labels=labels, **options)
plt.show()
class Weighted:
def __init__(self):
self.g = {}


# In[7]:


def add_node(self,node):
if node in self.g:
raise ValueError("Already exists")
self.g[node] = []


# In[8]:


def add_edge(self,src,dest,cost):
if src not in self.g or dest not in self.g:
raise ValueError("Src/dest not found")
children = self.g[src]
if dest not in children:
children.append((dest,cost))


# In[9]:


def get_neighbours(self,src):
neigh = []
if src not in self.g:
raise ValueError('Src not found')
for i in self.g[src]:
neigh.append(i[0])
return neigh


# In[10]:


def get_cost(self, src, dest):
cost = 0
if src not in self.g or dest not in self.g:
raise ValueError('Src/Dest not found')
for i in range(0,len(self.g[src])):
if self.g[src][i][0] == dest:
cost = self.g[src][i][1]
return cost


# In[11]:


def draw_graph(self):
G = nx.DiGraph()
for src in self.g:
G.add_node(src, label=src)
for dest in self.g[src]:


# In[12]:


def greedyBFS(graph, src, dest):
visited_nodes = []
que = PriorityQueue()
que.put((0, src))
min_cost = float('inf')
t_cost = 0
while que:
cost, node = que.get()
print(cost,node)
if node not in visited_nodes:
visited_nodes.append(node)
if node == dest:
print(t_cost,node)
return que
for i in graph.get_neighbours(node):
if i not in visited_nodes:
cost = graph.get_cost(node,i)
if cost < min_cost:
min_cost = cost
loc = i
que.put((min_cost,loc))
t_cost = t_cost + min_cost
return False
# ---------------------------------------------------------------------
def heuristic(graph, node, parent):
h_S = 8
h_S1 = 7
h_S2 = 3
h_S3 = 3


# In[13]:


h_G = 0
if node == 'S':
g_S = 0
f_n = g_S + h_S
return f_n
if node == 'S1':
g_S1 = graph.get_cost('S','S1')
f_n = g_S1 + h_S1
return f_n
if node == 'S2':
g_S2 = graph.get_cost('S','S2')
f_n = g_S2 + h_S2
return f_n
if node == 'S3':
g_S3 = graph.get_cost('S','S3')
f_n = g_S3 + h_S3
return f_n
if node == 'G':
if parent == 'S1':
g_G = graph.get_cost('S','S1') + graph.get_cost('S1','G')
f_n = g_G + h_G
return f_n
if parent == 'S2':
g_G = graph.get_cost('S','S2') + graph.get_cost('S2','G')
f_n = g_G + h_G
return f_n
if parent == 'S3':
g_G = graph.get_cost('S','S3') + graph.get_cost('S3','G')
f_n = g_G + h_G
return f_n
def Astar(graph, src, dest):
que = deque()


# In[14]:


que.append(src)
costs = []
path = []
parent = ''
lst = []
while que:
min_cost = float('inf')
for q in que:
print('1 node,parent',q,parent)
cost = heuristic(graph, q, parent)
print('2 node,cost',q,cost)
if cost < min_cost:
min_cost = cost
node = q
if node == dest:
return
que.remove(node)
print('3 Min:',node,min_cost)
path.append(node)
neigh = graph.get_neighbours(node)
for n in neigh:
print('4 n:',n)
if n == 'G':
if node == 'S1':
parent = 'S1'
if node == 'S2':
parent = 'S2'
if node == 'S3':
parent = 'S3'
que.append(n)
print('-------',path)


# In[15]:


g = Weighted()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_edge('A','B',12)
g.add_edge('A','C',2)
g.add_edge('B','D',7)
g.add_edge('C','D',4)
g.add_edge('C','G',1)
g.add_edge('D','G',2)
g.add_edge('F','A',1)
g.add_edge('F','G',5)
pprint.pprint(g.g)
greedyBFS(g,'A','G')
w = Weighted()
w.add_node('S')
w.add_node('S1')
w.add_node('S2')
w.add_node('S3')
w.add_node('G')
w.add_edge('S','S1',1)
w.add_edge('S','S2',5)
w.add_edge('S','S3',15)
w.add_edge('S1','G',10)
w.add_edge('S2','G',5)
w.add_edge('S3','G',5)
Astar(w,'S','G')


# In[ ]:





# In[ ]:




