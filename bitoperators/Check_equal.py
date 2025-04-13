def check(n1,n2):
    if (n1 ^ n2):
        print(f"The numbers {n1} and {n2} aren't the equal.")
    else:
        print(f"The numbers {n1} and {n2} are equal.")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
check(num1,num2)