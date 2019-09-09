#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 04:29:13 2017

@author: p2
"""

import pandas as pd
from sklearn.utils import shuffle
import pprint

df = pd.read_csv('merged.csv')
df_new  = df.dropna()

df_new = shuffle(df_new)
df_new = df_new.reset_index(drop=True)

c = 0
source_dict = {}
dict_for_list = {}
dest_list = []
for ix in range(500):
    source = "S("+str(df_new['source'][ix])+")"
    if source not in source_dict:
        l = []
        dest = "D("+str(df_new['destination'][ix])+")"
        l.append(dest)
        dict_for_list[source] = l
        source_dict[source] = dict_for_list[source]
    else:
        dest_list = dict_for_list[source]
        if df['destination'][ix] not in dest_list:
            dest = "D("+str(df_new['destination'][ix])+")"
            dest_list.append(dest)
        source_dict[source] = dest_list
    

        
import networkx as nx
h = nx.Graph(source_dict)
pos = nx.layout.fruchterman_reingold_layout(h)
nx.draw_networkx(h, pos,arrows=True,node_color='blue',edge_color='red',node_size=100)



h = nx.Graph()
for ix in range(500):
    h.add_edge("S("+str(df_new['source'][ix])+")","D("+str(df_new['destination'][ix])+")",width =2)
    h.add_edge("D("+str(df_new['destination'][ix])+")" ,"DP("+str(df_new['destinationPort'][ix])+")",width=2)
    h.add_edge("S("+str(df_new['source'][ix])+")" ,"SP("+str(df_new['sourcePort'][ix])+")",width=400)
pos = nx.layout.fruchterman_reingold_layout(h)
#nx.draw_networkx(h, pos)
nx.draw_networkx(h, pos,arrows=True,node_color='blue',edge_color='red',node_size=50,width=2,font_size = 2)

h = nx.DiGraph()

l1 = []
l2 = []
l3 = []
for ix in range(50):
    h.add_edge("S("+str(df_new['source'][ix])+")","D("+str(df_new['destination'][ix])+")")
    l1.append(("S("+str(df_new['source'][ix])+")","D("+str(df_new['destination'][ix])+")"))
    
    h.add_edge("D("+str(df_new['destination'][ix])+")" ,"DP("+str(df_new['destinationPort'][ix])+")")
    l2.append(("D("+str(df_new['destination'][ix])+")" ,"DP("+str(df_new['destinationPort'][ix])+")"))
    
    h.add_edge("S("+str(df_new['source'][ix])+")" ,"SP("+str(df_new['sourcePort'][ix])+")")
    l3.append(("S("+str(df_new['source'][ix])+")" ,"SP("+str(df_new['sourcePort'][ix])+")"))

pos = nx.layout.random_layout(h)
nx.draw_networkx(h,pos)
nx.draw_networkx_edges(h, pos, edgelist=l1, width=2, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(h, pos, edgelist=l2, width=2, alpha=0.5, edge_color='b')
nx.draw_networkx_edges(h, pos, edgelist=l3, width=2, alpha=0.5, edge_color='g')



























     