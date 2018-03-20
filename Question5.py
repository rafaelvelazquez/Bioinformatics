#Rafael Velazquez   Question5.py

def main():
    print("This program opens a user provided text file and returns a new file")
    print("with only the even numbered lines.")

    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    writeDoc = open('new' + str(docName), 'w') 

    counter = 0
    for line in openDoc:
        if counter%2 == 1:
            writeDoc.write(str(line))
        counter = counter + 1

main()
