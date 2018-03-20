def getNeighbors(pattern,d):
    # base case
    if d == 0:
        return [pattern]
    if len(pattern) ==1:
        return ["A","C","G","T"]

    # recursive case
    neighbors = []
    suffixN = getNeighbors(pattern[1:],d)
    for Text_nei in suffixN:
        if HamDist(pattern[1:], Text_nei) < d:
            # if the neighbor of the suffix has less than
            # d mismatches with suffix(pattern),
            # then the first character can be a mismatch
            for x in ["A","C","G","T"]:
                neighbors.append(x+Text_nei)
        else:
            # we've already used up all our mismatches
            # in the suffix
            neighbors.append(pattern[0]+Text_nei)
    return neighbors

        
def HamDist(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count
            


def main():
    f = open('all10mers.txt', 'w')
    a1 = getNeighbors("AAAAAAAAAA",10)
    for i in range(len(a1)):
        f.write(a1[i]+'\n')

main()
