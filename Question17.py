#Rafael Velazquez   Question17.py

from copy import *

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

def profileUpdate(patternList):
    '''Creates a profile matrix based on what patterns are in list
    Input: list(list with patterns/motifs)
    Output: double array/list (Profile matrix)'''

    #Updates double array/matrix based on patterns
    aProfile = []
    cProfile = []
    gProfile = []
    tProfile = []
    
    for i in range(len(patternList[0])):
    #for each index of a motif
        a = 0
        c = 0
        g = 0
        t = 0
        
        for j in range(len(patternList)):
        #for each motif in the list
            if patternList[j][i] == 'A':
                a = a + 1
            elif patternList[j][i] == 'C':
                c = c + 1
            elif patternList[j][i] == 'G':
                g = g + 1
            else: # patternList[j][i] == 'T':
                t = t + 1

        a = a / len(patternList) 
        c = c / len(patternList) 
        g = g / len(patternList) 
        t = t / len(patternList) 

        aProfile.append(a)
        cProfile.append(c)
        gProfile.append(g)
        tProfile.append(t)

    matrix = [aProfile,cProfile,gProfile,tProfile]

    return matrix
        
            
def mostProbablePatternInString(matrix,text,k):
    '''Detects the most probable k-mer in a string of dna
    Inputs: double array/list (profile matrix), string (DNA string), integer (size of k-mer)
    Outputs: string (most probable k-mer)'''

    #Sample maximum for comparison later
    d = {'blank' : -1}
    maximum = 'blank'

    #Most Probable String Implementation
    #-----------------------------------
    for i in range(len(text)- k + 1):
        pattern = text[i:i+k]

        total = 1
        for j in range(k):
            if text[i+j] == 'A':
                total = matrix[0][j] * total 
            elif text[i+j] == 'C':
                total = matrix[1][j] * total
            elif text[i+j] == 'G':
                total = matrix[2][j] * total
            else:# text[i+j] == 'T':
                total = matrix[3][j] * total

        d.update({pattern: total})

        if d[pattern] > d[maximum]:
            maximum = pattern

    return maximum
    

def greedyMotifSearch(dnaList, k, t):
    '''Finds the motif for a set of DNA strings using a greedy algorithm
    Inputs: array/list (all DNA strings), integer (size of k-mer), integer (size of array/list)
    Output: array/list (list of most probable motif)'''

    #Create a sample bestScore for checking against later
    bestScore = k * t + 1
    
    #All possible starter motifs    
    starterMotifs = []
    for i in range(len(dnaList[0]) - k + 1):
        starterMotifs.append(dnaList[0][i:i + k])

    #Greedy Motif Implementation
    #----------------------------
    for i in range(len(starterMotifs)):
       
        storage = []
        storage.append(starterMotifs[i])

        profileMatrix = profileUpdate(storage)
                   
        for j in range(1,t):
            storage.append(mostProbablePatternInString(profileMatrix, dnaList[j], k))
            profileMatrix = profileUpdate(storage)


        currentScore = score(storage)
        if currentScore < bestScore:
            bestMotifs = deepcopy(storage)
            bestScore = currentScore

    return bestMotifs
        

def main():
    print("This program implements a greedy motif search for a collection of DNA.")

    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    line1 = openDoc.readline().split()
    k, t = int(line1[0]), int(line1[1])

    dnaList = []
    for line in openDoc:
        dnaList.append(line.strip('\n'))

    bestGreedyMotif = greedyMotifSearch(dnaList, k, t)

    for i in range(len(bestGreedyMotif)):
        print(bestGreedyMotif[i])
main()  
