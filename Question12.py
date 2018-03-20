#Rafael Velazquez   Question12.py

def main():
    print("This program calculates the Hamming Distance between 2 DNA strings.")

    dna1 = str(input("Enter the first DNA sequence: ")).upper()
    dna2 = str(input("Enter the second DNA sequence: ")).upper()

    d = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            d = d + 1

    print(d)
main()
