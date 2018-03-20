#Rafael Velazquez   Question28.py

def flipSign(string):
    '''Takes a signed permuation and switches its sign
    Input: string
    Output: updated string'''

    if string[0] == '+':
        string = '-' + string[1:]

    else: #string[0] == '-':
        string = '+' + string[1:]

    return string

def traverse(aList,n):
    '''Finds the position in which n is located in the list
    Input: List, string(n)
    Output: int(postion)'''

    for i in range(len(aList)):
        if aList[i][1:] == n:
            return i

    
def flipList(aList,start,end):
    '''Takes a list and switches the order of it depending on start/end points
    Input: List([start,...,end]), int(start), int(end)
    Output: List in reverse order([end,...,start])'''

    temp = []
    for i in range(end,start,-1):
        #Includes everything from end but not including start
        temp.append(flipSign(aList[i]))
    #Add start to the end to compensate
    temp.append(flipSign(aList[start]))

    x = 0
    for i in range(start,end + 1):
        aList[i] = temp[x]
        x += 1
    

def printList(aList):
    '''Takes a list and returns a string representation of it
    Input: List
    Output: String '''

    string = ""

    for i in range(len(aList)):

        if i != len(aList) - 1:
            string = string + str(aList[i]) + ' '

        else: #i == len(aList) - 1
            string = string + str(aList[i])

    return "(" + string + ")"
    
    
def main():
    #Introduction
    print("This program implements greedy sorting.")

    #Open document
    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    #Create list representation
    sequence = openDoc.readline().split()

    #Remove parentheses
    sequence[0] = sequence[0][1:]
    sequence[len(sequence)-1] = sequence[len(sequence)-1][:-1]

    #Create a new document for storing result
    writeDoc = open('Solutions4' + str(docName),'w')
    
    #Implement Greedy Sorting
    for i in range(len(sequence)):
        if str(i+1) != sequence[i][1:]:
            j = traverse(sequence,str(i+1))
            flipList(sequence,i,j)
            writeDoc.write(printList(sequence)+'\n')

        if sequence[i][0] == '-':
            sequence[i] = flipSign(sequence[i])
            writeDoc.write(printList(sequence)+'\n')
            
main()

