def divide(dividend,divisor):
    if (dividend < 0) ^ (divisor < 0):
        sign = -1
    else:
        sign = 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    t = 0
    q = 0
    
    for i in range(31,-1,-1):
        if t + (divisor << i) <= dividend:
            t += divisor << i

            q += 1 << i

    if sign == -1:
        q = -q
    return q

print(divide(20,3))
