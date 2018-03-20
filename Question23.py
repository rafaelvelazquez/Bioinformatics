#Rafael Velazquez   Question23.py
        

def main():

    #Introduction
    print("This program finds the length of a longest path in the Manhattan Tourist Problem.")

    #Open document
    docName = input("Please enter the name of the text file with extension: ")
    openDoc = open(str(docName),'r')

    #Get numbers to see how much to read into document
    down,right = openDoc.readline().split()

    down = int(down)
    right = int (right)

    #Create down matrix
    dnMatrix = []
    
    for i in range(down):
        dnMatrix.append(list(openDoc.readline().split()))

    #Skip line
    openDoc.readline()

    #Create right matrix
    rtMatrix = []

    for i in range(down + 1):
        rtMatrix.append(list(openDoc.readline().split()))

    #Create Partial Grid
    gridMatrix = []

    for i in range(down + 1):
        gridMatrix.append(list())

        #**Create TopMostRow**
        if i == 0:
            gridMatrix[0].append(0)

            for j in range(right):
                gridMatrix[0].append(gridMatrix[0][j] + int(rtMatrix[0][j]))

        #**Create LeftMostColumn**
        else: # i >= 1
            gridMatrix[i].append(gridMatrix[i-1][0] + int(dnMatrix[i-1][0]))


    #Fill in rest of Grid, 1 row at a time
    for i in range(1,down + 1):
        
        for j in range(right):
            rightEdge = gridMatrix[i][j] + int(rtMatrix[i][j])
            downEdge = gridMatrix[i-1][j+1] + int(dnMatrix[i-1][j+1])
            if rightEdge >= downEdge:
                gridMatrix[i].append(rightEdge)
            else: # downEdge > rightEdge
                gridMatrix[i].append(downEdge)

    #Result: last entry in grid matrix with position (down,right)
    print(gridMatrix[down][right])
        
main()




