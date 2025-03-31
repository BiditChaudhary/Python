file = open("Codingal.txt","r")
print("The first 8 characters of the file are:")
print(file.read(8))

print("The following is the entire content of the file:")
print(file.read())
file.close()

file = open("Codingal.txt","a+")
file.write("\n I am a penguin. \n I am 1 year old.")
file.seek(0)
print(file.read())
file.close()