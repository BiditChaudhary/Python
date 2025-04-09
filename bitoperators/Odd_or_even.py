def isoddoreven(n):
    if n ^ 1 == n + 1:
        return True
    else:
        return False
    
n = int(input("Enter you number: "))
if isoddoreven(n):
    print("It is an even number.")
else:
    print("It is an odd number.")