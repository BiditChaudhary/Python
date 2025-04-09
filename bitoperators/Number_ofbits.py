def numofbits(n):
    count = 0
    while n:
        count += 1
        n = n>>1
    print(count)

num1 = int(input("Enter you number: "))
numofbits(num1)