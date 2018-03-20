#Rafael Velazquez   Question9.py

def skew(genome):
    c = 0   #Number of C's
    g = 0   #Number of G's
    temp = 0     #Temp value for minimum 
    minList = []   #Place to hold all positions for when G-C is at its lowest

    for i in range(len(genome)):
        if genome[i] == 'C':
            c = c + 1
        elif genome[i] == 'G':
            g = g + 1
        else:
            continue
        
        skew = g - c
        #print(skew) ##Visual reference to see lowest skew

        if skew < temp:
            minList = [i]
            temp = skew
        elif skew == temp:
            minList.append(i)
        else:
            continue
        
    return minList
    
def main():
    print("This program finds the position(s) in a genome minimizing the skew.")
    print("Denoted as the difference between G's to C's.")

    genome = str(input("Enter the DNA sequence for the genome: ")).upper()
    minList= skew(genome)

    for i in range(len(minList)):
        print(int(minList[i]) + 1,end= " ")
main()


