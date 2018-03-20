#Rafael Velazquez   Question3.py

def main():
    print("This program will slice a string into two substrings.")
    print("One from a to b and the other from c to d.")

    print("Please enter a string that is at most 200 characters long: ")
    s = input("")

    while len(s)> 200:
        print("Please enter a string that is at most 200 characters long: ")
        s = input("")

    a,b,c,d = eval(input("Please enter interger values for a,b,c,d using commas: "))
    print(s[a:b+1],s[c:d+1])
        

main()
        
    
