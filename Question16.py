#Rafael Velazquez   Question16.py

def main():
    print("This program finds the most probable k-mer in a string")
    print("using a 4 by k matrix Profile.")

    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')
    text = openDoc.readline()
    k = eval(openDoc.readline())
    listA = list(openDoc.readline().split())
    listC = list(openDoc.readline().split())
    listG = list(openDoc.readline().split())
    listT = list(openDoc.readline().split())

    for i in range(len(listA)):
        listA[i] = eval(listA[i])
        listC[i] = eval(listC[i])
        listG[i] = eval(listG[i])
        listT[i] = eval(listT[i])

    d = {'blank' : 0}
    maximum = 'blank'
    
    
    for i in range(len(text)- k + 1):
        pattern = text[i:i+k]
        if pattern not in d:
            total = 1
            for x in range(k):
                if text[i+x] == 'A':
                    total = total * listA[x]
                elif text[i+x] == 'C':
                    total = total * listC[x]
                elif text[i+x] == 'G':
                    total = total * listG[x]
                else: #text[i+x] == 'T':
                    total = total * listT[x]

            d.update({pattern: total})
            
        if d[pattern] > d[maximum]:
            maximum = pattern

    print(maximum)

main()
