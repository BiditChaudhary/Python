file1 = open("file1","r")
print(file1.read())
file1.close()

file1 = open("file1","w")
file1.write("I am Bidit, I am 13 years old.")
file1.close()

file1 = open("file1","a")
file1.write("I am a penguin and I am 1 year old.")
file1.close()

file1 = open("file1","r")
print("**This is the uptated file:**")
print(file1.read())
file1.close()