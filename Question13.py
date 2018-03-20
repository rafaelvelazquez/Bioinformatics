#Rafael Velazquez   Question13.py

def hamDistRange(pattern1, pattern2, d):
    correct = 0
    error = 0
    for i in range(len(pattern1)):
        if pattern1[i] == pattern2[i]:
            correct = correct + 1
        else:
            error = error + 1

        if correct >= len(pattern1) - d:
            return True

        if error > d:
            return False


    
def main():
    print("This program finds all occurences of a pattern in a string")
    print("with at most d mismatches.")

    pattern = input("Enter the substring that will act as the pattern for the search: ")
    dna = input("Enter the text sequence that will act as the field for the search: ")
    mismatch = eval(input("Enter the amount of mismatches your willing to have: "))

    for i in range(len(dna) - len(pattern) + 1):
        if hamDistRange(pattern,dna[i : i+ len(pattern)], mismatch):
            print(i,end=' ')
    
main()
