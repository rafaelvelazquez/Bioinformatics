#Rafael Velazquez   Question8.py

def main():
    print("This program counts and returns the occurence of a substring within a string.")

    subString = input("Enter the substring you want to count the occurences for: ")
    string = input("Enter the string your checking for substring patterns : ")
    occur = ""

    for i in range(len(string) - len(subString) + 1):
        if subString == string[i : i + len(subString)]:
            occur = occur + str(i) + " "

    print(occur)
main()
