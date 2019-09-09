#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:40:06 2017

@author: p2
"""

import networkx as nx
import pandas as pd

data = pd.read_csv("merged.csv")

x=data[['source','destination']]

g1=nx.Graph()
g1.add_edge(1,2)
g1.add_edge(1,3)

G = nx.Graph()
for i in range(100):
    G.add_edge("S"+str(x['source'][i]),"D"+str(x['destination'][i]),weight=data['totalSourcePackets'][i])
    
"""   
src_port = data[['source','sourcePort']]
des_port = data[['destination','destinationPort']]    

for i in range(100):
    G.add_edge("SP"+str(src_port['sourcePort'][i]),"S"+str(src_port['source'][i]))
    
for i in range(100):
    G.add_edge("DP"+str(des_port['destinationPort'][i]),"D"+str(des_port['destination'][i]))
"""

arc_weight=nx.get_edge_attributes(G,'weight')

nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G),edge_labels=arc_weight,node_size=5 ,with_labels=True , font_size=5)
   
        
import matplotlib.pyplot as plt
#G = nx.petersen_graph()
#plt.subplot(121)
nx.draw(G,node_size=5 ,with_labels=True , font_size=5)
#nx.draw(g1,node_size=2 ,with_labels=True)
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=False )

mal = data[['sourcePort','source','destination' , 'destinationPort','destinationTCPFlagsDescription','protocolName' ]]

mal = mal[mal.protocolName != "udp_ip"]

import numpy as np
mal = mal[pd.notnull(mal['destinationTCPFlagsDescription'])]

mal = mal.reset_index(drop=True)


for i in range(1000):
    mal['destinationTCPFlagsDescription'][i]=str(mal['destinationTCPFlagsDescription'][i]).split(',')


for i in range(1000):
    if 'S' not in mal['destinationTCPFlagsDescription'][i]:
        mal.drop(i,axis=0)

mal = mal.reset_index(drop=True)

chk = mal[mal.source =='192.168.2.107']



    









