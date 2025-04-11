def number_of_bits(n):

    ones = 0 
    zeros = 0
    print(ones,zeros)
    while (n):
        if n&1 == 1:
            ones += 1

        else:
            zeros += 1
        
        n>>=1

    print("The number of ones is",ones,"\n The number of zeros is",zeros)
number_of_bits(5)