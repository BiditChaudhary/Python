def compute_power(x,y):
    result = 1
    while (y > 0):
        if (y % 2 == 0):
            x = x * x
            y >>= 1

        else:
            result = result * x
            y = y - 1

    return result

x = int(input("Enter a number for the base: "))
y = int(input("Enter a number for the power: "))
print(compute_power(x,y))