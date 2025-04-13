def oneodd(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res

arr = [3,3,4,4,5,5,6]
print(f"The one odd number in the array is {oneodd(arr)}.")