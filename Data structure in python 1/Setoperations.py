My_set = {1,2,2,3,4,4}
print("My set:",My_set)
My_set.add(5)
print("Uptated set:",My_set)

Set1 = My_set
Set2 = {1,2,6,9}

print(Set1.difference(Set2))
print(Set1.symmetric_difference(Set2))