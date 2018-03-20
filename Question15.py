#Rafael Velazquez   Question15.py

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
    print("This program computes the distance between a pattern and a collection")
    print("of DNA strings.")

    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')
    pattern = str(openDoc.readline().strip('\n'))
    listOfDNA = openDoc.read().split()

    dist = distBtwnPatAndString(pattern, listOfDNA)

    print(dist)
    

main()
