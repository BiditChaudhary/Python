def power_of_four(n):
    count = 0
    if (n & (~(n & (n - 1))) > 1):
        while(n & (~(n & ( n - 1))) > 1):
            n >>= 1
            count += 1
        if count % 2 == 0:
            return True
        else: 
            return False
        
number = int(input("Enter a number: "))
result = power_of_four(number)
if result:
    print(f"{number} is a power of 4.")
else:
    print(f"{number} is not a power of 4.")