def poweroftwo(n):
    if (n == 0):
        return 0
    elif (n & (~(n - 1))== n):
        return 1
    else:
        return 0
    
Number = int(input("Enter a number: "))
if (poweroftwo(Number)):
    print(f"{Number} is a power of 2.")

else:
    print(f"{Number} is not a power of two.")