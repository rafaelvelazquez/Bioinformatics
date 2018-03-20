#Rafael Velazquez   Question6.py

def main():
    print("This program calculates how many times each word has appeared in a string.")
    String = input("Please enter a string of at most 10000 characters: ")

    while len(String) > 10000:
        String = input("Please enter a string of at most 10000 characters: ")

    d = {}

    for word in String.split(' '):
        if word not in d:
            d[word] = 1
        else:
            current = d[word] 
            d[word] = current + 1

    for key, value in d.items():
        print (key,value)

main()
            
