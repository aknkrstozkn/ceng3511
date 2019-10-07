#!/usr/bin/python3

import sys,re
from ast import literal_eval

text = open(str(sys.argv[1]),"r") 

graph = text.readlines()

def GraphToDictionary(graph):
    graph[0] = re.sub(r"([A-Z])", r"'\1'", graph[0])    

    string = '{' + graph[0]
    for i in range(1,len(graph)):
        graph[i] = re.sub(r"([A-Z])", r"'\1'", graph[i])
        
        string += "," + graph[i]

    string += "}"
    dic = literal_eval(string)
    newDic = {}
    for element in dic:
        oldDic = literal_eval(str(dic[element]))
        newChild = {}        
        for key in oldDic:            
            if int(oldDic[key]) != 0:
                newChild[key] = oldDic[key]
        newDic[element] = newChild            
    return newDic
    

dic = GraphToDictionary(graph)

print(dic)



