def flip_bits(a,b):
    x = a ^ b
    count = 1
    while (x & (x - 1) > 0):
        count += 1
        x = x & (x - 1)

    print(f"The number of bits to be flipped is {count}")

flip_bits(4,2)