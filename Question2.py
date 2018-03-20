#Rafael Velazquez   Question2.py

def main():

    print("This program returns the square of the hypotenuse of a right triangle")
    print("with lengths a and b.")
    print("Please enter two intergers that are less than 1000 for lengths a and b.")
    a,b = eval(input("(Please seperate using comma... i.e 10, 4) : "))

    while (a >= 1000) or (b >= 1000):
        a,b = eval(input("Please enter two intergers that are less than 1000: "))

    c = (a**2) + (b**2)
    print(a, '^2 +', b, '^2 = ')
    print(a**2, '+', b**2, '=', c) 
main()
        
