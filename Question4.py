#Rafael Velazquez   Question4.py

def main():
    print("This program takes the sum of all odd numbers between a and b.")

    a,b = eval(input("Please enter two values for a and b that satisfy a < b < 10000: "))

    while (a >= b) or (b >= 10000):
        a,b = eval(input("Please enter two values for a and b that satisfy a < b < 10000: "))
        
    temp = 0

    if a%2 == 1 and b%2 == 0:
        for i in range(a,b,2):
            temp = temp + i
        print(temp)

    elif a%2 == 1 and b%2 == 1:
        for i in range(a,b,2):
            temp = temp + i
        temp = temp + b
        print(temp)

    elif a%2 == 0 and b%2 == 0:
        for i in range(a+1,b,2):
            temp = temp + i
        print(temp)

    else:
        for i in range(a+1,b,2):
            temp = temp + i
        temp = temp + b
        print(temp)                
        
main()        
               
