Content = open("Text.txt","r")
r = Content.read()

Counter = 0
Clist = r.split("\n")
for i in Clist:
    Counter += 1

print(f"There are {Counter} lines in the file 'Content'. ")