#Rafael Velazquez   Question14.py

def hamDist(pattern1,pattern2):
    d = 0

    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            d = d + 1

    return d

def distBtwnPatAndString(pattern, dna):
    total = 0

    for i in range(len(dna)):
        hamdist = len(pattern) + 1

        for x in range(len(dna[i]) - len(pattern) + 1):
            current = hamDist(pattern,dna[i][x : x + len(pattern)])
            if hamdist > current:
                hamdist = current

        total = total + hamdist

    return total
    
def main():
    print("This program calculates the median string of length k from a")
    print("collection of strings.")

    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')
    k = int(openDoc.readline())
    kmers = []
    alldna = []

    #Saved text files for all kmers size 1-10 to save time
    #-----------------------------------------------------
    openKmer = open('all' + str(k) + 'mers.txt', 'r') 

    for line in openKmer:
        kmers.append(line.strip('\n'))
    #-----------------------------------------------------

    for line in openDoc:
        alldna.append(line.strip('\n'))
        
    minimum = 'max'
    d = {'max' : len(alldna) * len(alldna[0])+ 1}

    #For all kmers
    for num in range(len(kmers)):
        dist = distBtwnPatAndString(kmers[num], alldna)
        d.update({kmers[num] : dist})
        if d[minimum] > d[kmers[num]]:
            minimum = kmers[num]

    print(minimum)

main()
