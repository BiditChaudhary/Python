def nthbit(n,k):

    if n & (1<<(k-1)):
        return "set"
    else:
        return "Not set"
n = 23
k = 4
print(f"The {k}th bit in {n} is",nthbit(n,k))
