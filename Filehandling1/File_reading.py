#File handling, reading a file

file1 = open("Text.txt","r")
r = file1.read()
print(r)
file1.close()

file1 = open("Text.txt","a")
file1.write("This is the final update.")
file1.close()

file1 = open("Text.txt","r")
r = file1.read()
print(r)
file1.close()