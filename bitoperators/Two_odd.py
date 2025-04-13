def twoodd(arr,size):
    xor_of_2 = arr[0]
    x = 0
    y = 0
    set_bit = 0
    for i in range(1, size):
        xor_of_2 = xor_of_2 ^ arr[i]
    set_bit = xor_of_2 & ~(xor_of_2 - 1)
    for i in range(size):
        if arr[i] & set_bit:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print(f"The two odd occuring numbers are {x} and {y}.")

arr = [2,2,3,3,4,5]
twoodd(arr,len(arr))
        