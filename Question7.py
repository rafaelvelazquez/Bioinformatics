#Rafael Velazquez   Question7.py

def main():
    print("This program computes the reverse complement of a DNA sequence.")

    dna = input("Enter DNA sequence: ")
    dna.upper() #Capitalize all letters in sequence
    newDna = ""
    counter = -1
    
    for ch in dna:
        if dna[counter] == 'A':
            newDna =  newDna + 'T'
            
        elif dna[counter] == 'C':
            newDna =  newDna + 'G'
            
        elif dna[counter] == 'G':
            newDna =  newDna + 'C'

        else:  # dna[counter] = 'T'
            newDna =  newDna + 'A'
            
        counter = counter - 1

    print(newDna)

main()
