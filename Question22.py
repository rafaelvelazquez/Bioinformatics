#Rafael Velazquez   Question22.py
        
from copy import deepcopy
from random import randrange

def makeDict(line,adjList,moves):
    '''Sets up adjacency list and calculates total number of edges/moves
    Inputs: string(Example: 10 -> 2,3 ), dictionary(empty), integer(0)
    Output: dictionary(updated with pairings),integer(total number of edges/moves)'''
    
    nodes = line.split(sep=' -> ')
    start = deepcopy(nodes[0])
    outNode = deepcopy(nodes[1].split(sep=','))
    moves = moves + len(outNode)
    adjList[start] = outNode

    return adjList,moves

def reconfigurePath(eulerCycle,position):
    '''Reconfigures the eulerian path from a new start point based on position
    Inputs: list(path so far), integer(location of new start point if first point of list = 1)
    Output: list(new path) '''
    
    newPath = []
    length = len(eulerCycle)

    #Append what was to right of the position till the end of the list
    for i in range(length - position,length):
        newPath.append(eulerCycle[i])

    #Append what was second in the list till the position
    for i in range (1, length - position + 1):
        newPath.append(eulerCycle[i])

    newCycle = deepcopy(newPath)
    return newCycle

def retraceSteps(adjList,eulerCycle):
    '''Finds a node that has an edge that was not visited by taking path backwards
    **Only call this function if you know there was an unvisted edge**
    Inputs: dictionary(adjacency list), list(path so far)
    Outputs: string(cuurent node), list(new path)'''
    
    newPosition = 1
    node = eulerCycle[len(eulerCycle)- newPosition]

    while len(adjList[node]) == 0:
        newPosition += 1
        node = eulerCycle[len(eulerCycle)- newPosition]

    newEulerCycle = reconfigurePath(eulerCycle,newPosition)
    return node, newEulerCycle


def traverse(node,adjList,eulerCycle):
    '''Follows along an adjacency list given a node and updates path taken
    Inputs: string(starting node), dictionary(adjacency list), list(path so far)
    Outputs: string(new starting node), dict(adjacency list updated), list(new path)'''
    
    if len(adjList[node]) != 0:
        num = randrange(0,len(adjList[node]))
        nextNode = adjList[node][num]
        eulerCycle.append(nextNode)
        adjList[node].remove(nextNode)
        
    else: #len(adjList[node]) == 0
        newNode, eulerCycle = retraceSteps(adjList,eulerCycle)
        num = randrange(0,len(adjList[newNode]))
        nextNode = adjList[newNode][num]
        eulerCycle.append(nextNode)
        adjList[newNode].remove(nextNode)


    return nextNode,adjList,eulerCycle
        

def main():

    #Introduction
    print("This program finds the Eulerian cycle in a graph.")

    #Gather all data needed
    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    adjList = {}
    totalNodes = 0
    totalMoves = 0

    for line in openDoc: 
        adjList,totalMoves = makeDict(line.strip('\n'),adjList,totalMoves)
        totalNodes += 1

    #Get random start point
    adjKeys = list(adjList.keys())
    startNode = adjKeys[randrange(0,totalNodes)]

    #Create Eulerian Cycle
    eulerCycle = [startNode]

    while totalMoves != 0:
        startNode,adjList,eulerCycle = traverse(startNode,adjList,eulerCycle)
        totalMoves -= 1

        
    #Store data in new doc
    newDoc = open('ResultsFor' + docName, 'w')
    for i in range(len(eulerCycle)):
        if i == len(eulerCycle) - 1:
            newDoc.write(eulerCycle[i])
        else:
            string = str(eulerCycle[i])+'->'
            newDoc.write(string)

main()

def test1():
    #reconfigurePath test from letter c
    x = ['a','b','c','f','a']
    position = 3
    print(reconfigurePath(x,position))

def test2():
    #retraceSteps test from a back to c
    adj = {'a': [], 'b': [], 'c': ['d'], 'f': [] }
    cycle = ['a','b','c','f','a']
    x,y = retraceSteps(adj,cycle)
    print(x,y)
