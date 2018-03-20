#Rafael Velazquez   Question10.py

def patternToNum(pattern):
    d = {'A':0, 'C':1, 'G':2, 'T':3}
    total = 0
    index = len(pattern) - 1

    for i in range(len(pattern)):
        if i == len(pattern) - 1: #If last letter
            total = total + d[pattern[i]]
        else: 
            total = total +  ( (4 ** index) * d[pattern[i]] )
            index = index - 1

    return total

def main():
    print("This program converts a DNA string to a number representation.")

    dna = str(input("Enter the DNA string: ")).upper()

    number = patternToNum(dna)

    print(number)

main()

