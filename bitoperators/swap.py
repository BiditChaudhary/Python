def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swapping, the value of a is {a}. \n After swapping, the value of b is {b}")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
swap(a,b)