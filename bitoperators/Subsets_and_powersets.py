def print_power_set(set,size):
    subsetsize = 1 << size
    subset = []
    
    for i in range(subsetsize):
        list = []
        for j in range(size):

            if i & (1 << j):
                list.append(set[j])

        subset.append(list)
    print(subset)

size = int(input("Enter the array size"))

set = []
for i in range(0,size):
    n = int(input("Enter the element: "))
    set.append(n)

print_power_set(set,size)