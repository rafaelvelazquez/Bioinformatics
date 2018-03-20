#Rafael Velazquez   Question18.py

from random import randint
from copy import deepcopy

def score(motifsList):
    '''Calculates the score from a set of motifs
    Input: array/list (set of motifs)
    Output: integer (score) '''
    
    #Score = the number of unpopular letters in Motifs
    total = 0
    
    for i in range(len(motifsList[0])):
    #for each index of a motif
        a = 0
        c = 0
        g = 0
        t = 0
        
        for j in range(len(motifsList)):
        #for each motif in the list
            if motifsList[j][i] == 'A':
                a = a + 1
            elif motifsList[j][i] == 'C':
                c = c + 1
            elif motifsList[j][i] == 'G':
                g = g + 1
            else: # motifsList[j][i] == 'T':
                t = t + 1

        total = total + len(motifsList) - max(a,c,g,t)

    return total

def generateProfile(patternList):
    '''Creates a profile matrix based on what patterns are in list
    Input: list(list with patterns/motifs)
    Output: double array/list (Profile matrix)'''

    #Updates double array/matrix based on patterns
    aProfile = []
    cProfile = []
    gProfile = []
    tProfile = []

    kmerSize = len(patternList[0])
    for i in range(kmerSize):
    #for each index of a motif/kmer
        a = 0
        c = 0
        g = 0
        t = 0
        
        for j in range(len(patternList)):
        #for each motif in the list of motifs
            if patternList[j][i] == 'A':
                a = a + 1
            elif patternList[j][i] == 'C':
                c = c + 1
            elif patternList[j][i] == 'G':
                g = g + 1
            else: # patternList[j][i] == 'T':
                t = t + 1

        #The plus 1's are to take into account pseudocounts.
        a = (a + 1) / (len(patternList) + 1)
        c = (c + 1) / (len(patternList) + 1)
        g = (g + 1) / (len(patternList) + 1)
        t = (t + 1) / (len(patternList) + 1)

        aProfile.append(a)
        cProfile.append(c)
        gProfile.append(g)
        tProfile.append(t)

    matrix = [aProfile,cProfile,gProfile,tProfile]

    return matrix

def mostProbableMotifSet(matrix,dnaList,k):
    '''Detects the most probable k-mers from a set of dna strings
    Inputs: double array/list (profile matrix), list (all DNA strings), integer (size of k-mer)
    Outputs: list (most probable k-mers)'''


    #Stores best motifs/kmers
    bestKmers = []

    #Most Probable Motif Set Implementation
    #--------------------------------------
    for x in range(len(dnaList)):

    #Sample maximum for comparison later
        d = {'blank' : -1}
        maximum = 'blank'
        
        for i in range(len(dnaList[x])- k + 1):
            pattern = dnaList[x][i:i+k]

            total = 1
            for j in range(k):
                if dnaList[x][i+j] == 'A':
                    total = matrix[0][j] * total 
                elif dnaList[x][i+j] == 'C':
                    total = matrix[1][j] * total
                elif dnaList[x][i+j] == 'G':
                    total = matrix[2][j] * total
                else:# dnaList[x][i+j] == 'T':
                    total = matrix[3][j] * total

            d.update({pattern: total})

            if d[pattern] > d[maximum]:
                maximum = pattern

        bestKmers.append(maximum)
                

    return bestKmers
    

def randomizedMotifSearch(dnaList,k,t):
    '''Randomly finds the best set of motifs from a set of DNA strings
    Inputs: list(list of DNA strings), integer(size of kmer/motif), integer(size of dnaList)
    Output: list (list of most probable set of kmers)'''

    motifs = [] #The set of motifs that will constantly keep updating
    bestMotifs = [] #The best set of motifs stored here
    for i in range(t):
        x =  randint(0,len(dnaList[i]) - k)
        motifs.append(dnaList[i][x:x+k])
        bestMotifs.append(dnaList[i][x:x+k])

    bestScore = score(bestMotifs)
    bestScoreNotFound = True

    while bestScoreNotFound:

        profile = generateProfile(motifs)
        motifs =  mostProbableMotifSet(profile,dnaList,k)
        newScore = score(motifs)

        if newScore < bestScore:
            bestMotifs = deepcopy(motifs)
            bestScore = newScore
        else:
            #Exit Loop
            ##To see what's being returned --> print(bestMotifs,bestScore)
            return bestScore, bestMotifs

    
        
def main():

    #Introduction
    print("This program implements a randomized motif search for a collection of DNA")
    print("to produce the most probable set of motifs.")

    #Gather all data needed
    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    line1 = openDoc.readline().split()
    k, t = int(line1[0]), int(line1[1])

    dnaList = []
    for line in openDoc:
        dnaList.append(line.strip('\n'))

    #Set example place holders for comparsion later
    bestRandomMotifs = ['placeholder']
    bestRandomScore = k * t 

    #Best RandomMotifSearch out of 1000 tries
    for i in range(1000):
        currentScore, currentList = randomizedMotifSearch(dnaList,k,t)
        if currentScore < bestRandomScore:
            bestRandomScore = currentScore
            bestRandomMotifs = deepcopy(currentList)

    #Print out motifs
    for i in range(len(bestRandomMotifs)):
        print(bestRandomMotifs[i])

main()

