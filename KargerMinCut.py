# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:06:48 2015

@author: chiarabiscaro
"""
import csv, random, copy

def MinCut(graph):
    """
    Karger algorithm for finding mincuts in a graph expressed as an adjecency
    list in a dictionary. Returns numer of crossing edges
    """
    
    if len(graph) <= 2:
        for key in graph:
            edges = len(graph[key])
        return edges
        
    while True:
        rand_1 = random.choice(graph.keys())
        if graph[rand_1]:
            rand_2=random.choice(graph[rand_1])
            break
        
    graph2 = copy.deepcopy(graph)
        
    for key in graph: #remove 1st node and replace with second
        for i in range(0,len(graph[key])-1):
            if graph2[key][i] == rand_1:
                graph2[key].pop(i)
                graph2[key].append(rand_2)
                graph2[rand_2].append(key)
            
            if graph2[key][i] == key:
                graph2[key].pop(i)
                    
    for i in range(0,len(graph[rand_2])-1): #remove 1st node from second 
        if graph2[rand_2][i] == rand_1:
            graph2[rand_2].pop(i)
    
    graph2.pop(rand_1) # remove 1st node 
    MinCut(graph2)


#integer_file = open("kargerMinCut.txt", 'r')

graph_dic = {} 
graph_list = []
#line_list = integer_file.readlines()
#for number_list in line_list:
#    graph_dic[int(number_list[0])] = [x for x in number_list[1:]]
    
with open("kargerMinCut.txt", 'r') as int_file:
    for line in csv.reader(int_file, delimiter="\t"):
        graph_list.append(line)

for number_list in graph_list:
    graph_dic[int(number_list[0])] = [int(x) for x in number_list[1:-1]]

test = {1:[2],2:[1,3],3:[2],4:[2]}

mins = 300
#for i in range(0,500):
new_cut=MinCut(test)
#    if new_cut < mins:
#        mins = new_cut
print new_cut