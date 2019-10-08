#SheBang For Scripting
#!/usr/bin/python3

#Regex and System Packages
import sys,re,operator,collections
#Package For Better Dictionary Parsing
from ast import literal_eval

#Getting Input File As A Only Readable File From Commend Argumant
text = open(str(sys.argv[1]),"r") 
#Reading All Lines From Input File And Holding These Lines As A List
graph = text.readlines()

#######----Converting Input-Graph To Dictionary----#######
def GraphToDictionary(graph):
    #Adding Double Quotes(") To The Beginning And The End Of Letters For Dictionary Syntax
    graph[0] = re.sub(r"([A-Z])", r"'\1'", graph[0])    
    
    ###--Colliding Graph Lines And Creating A Dictionary From Them--###
    string = '{' + graph[0]
    for i in range(1,len(graph)):
        #Adding Double Quotes(") To The Beginning And The End Of Letters For Dictionary Syntax
        graph[i] = re.sub(r"([A-Z])", r"'\1'", graph[i])
        
        string += "," + graph[i]
    string += "}"
    dic = literal_eval(string)
    ###--Colliding Graph Lines And Creating A Dictionary From Them--###
    
    ###--Also, Converting All Graph Lines To Dictionary--###
    newDic = {}
    for element in dic:
        oldDic = literal_eval(str(dic[element]))
        newChild = {}        
        for key in oldDic:
            #If Keys Hold Zero Values, Not Adding Them To Dictionaries Because No Need Them
            #Basicly we are clearing zero values.
            if int(oldDic[key]) != 0:
                newChild[key] = oldDic[key]
        newDic[element] = newChild   
    ###--Also, Converting All Graph Lines To Dictionary--###
    return newDic
    
dic = GraphToDictionary(graph)
#######----Converting Input-Graph To Dictionary----#######

#######----Getting Start and Goal Keys As Console Inputs----#######
startKey = str(input("Please enter the start state : "))
goalKey = str(input("Please enter the goal state : "))
#######----Getting Start and Goal Keys As Console Inputs----#######

#############################################------Searching Algorithms------#############################################

#######----Breadth-First Search----#######
def BreadthFirstSearch(dic, goalKey, startKey):
    #Creating List For Visited Values
    visited = []
    #Adding Start Key Beginning Of The Script Because We Always Visit It
    visited.append(startKey)
    #Creating Queue For BFS usage(Its Techniclay Not A Queue But We Use It Like Queue)
    queue = []
    #Creating A List To Hold Paths(Also This List Works As Queue)
    stringList = []
    
    ###--Recursive Implementation Of Recursive Breadth-First Search--###
    def BFS(string, key):
        #If We Hit Goal Then Return Path
        if key == goalKey:
            return string;
        #If We Dont Hit Yet Than Appending Not Visited Keys And Their Paths
        else:        
            for item in dic[key]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
                    stringList.append(string + " - " + item)
            return BFS(stringList.pop(0), queue.pop(0))            
    ###--Recursive Implementation Of Recursive Breadth-First Search--###
    print("BFS : " + BFS(startKey,startKey))

BreadthFirstSearch(dic, goalKey, startKey)
#######----Breadth-First Search----#######

#######----Depth-First Search----#######
def DepthFirstSearch(dic, goalKey, startKey):
    #Creating List For Visited Values
    visited = []
    #Adding Start Key Beginning Of The Script Because We Always Visit It
    visited.append(startKey)
    #Creating Stack For DFS usage(Its Techniclay Not A Stack But We Use It Like Stack)
    stack = []
    #Creating A List To Hold Paths(Also This List Works As Stack)
    stringList = []
    
    ###--Recursive Implementation Of Recursive Depth-First Search--###
    def DFS(string, key):
        returnKey = None
        
        #If We Hit Goal Then Return Path
        if key == goalKey:
            return string;
        #If We Dont Hit Yet Than Appending Not Visited Keys And Their Paths
        else:        
            for item in dic[key]:
                if item not in visited:
                    stack.append(item)
                    visited.append(item)
                    stringList.append(string + " - " + item)
                    returnKey = item
                    break
            if returnKey is None:
                stringList.pop()
                stack.pop()
                return DFS(stringList[-1], stack[-1])
            
            return DFS(stringList[-1], stack[-1])            
    ###--Recursive Implementation Of Recursive Depth-First Search--###
    print("DFS : " + DFS(startKey,startKey))

DepthFirstSearch(dic, goalKey, startKey)
#######----Depth-First Search----#######

#######----Uniform-Cost Search----#######
def UniformCostSearch(dic, goalKey, startKey):    
    #Creating List For Visited Values
    visited = []
    #Adding Start Key Beginning Of The Script Because We Always Visit It
    visited.append(startKey)
    #Creating Queue For UCS usage(Its Techniclay Not A Queue But We Use It Like Queue)
    queue = []
    #Creating A List To Hold Paths(Also This List Works As Queue)
    stringList = []
    
    #Shortind Dictionaries By Value To Get Least Cost Path
    def ShortingDictionary(dic):
        newDic = {}
        for dictionary in dic:
            secondDic = {}
            for key, value in sorted(dic[dictionary].items(), key=lambda kv: kv[1], reverse=False):
                secondDic[key] = value
            newDic[dictionary] = secondDic   
        return newDic    
    
    dic= ShortingDictionary(dic)
    ###--Recursive Implementation Of Recursive Uniform-Cost Search--###
    def UCS(string, key):
        #If We Hit Goal Then Return Path
        if key == goalKey:
            return string;
        #If We Dont Hit Yet Than Appending Not Visited Keys And Their Paths
        else:            
            for item in dic[key]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
                    stringList.append(string + " - " + item)
            return UCS(stringList.pop(0), queue.pop(0))            
    ###--Recursive Implementation Of Recursive Uniform-Cost Search--###
    print("UCS : " + UCS(startKey,startKey))



UniformCostSearch(dic, goalKey, startKey)
#######----Uniform-Cost Search----#######