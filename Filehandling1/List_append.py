file1 = open("sample_doc.txt","r")
file2 = open("Codingal.txt","r")
print("The following are the contents of the first file:")
print(file1.read())
print()
print("The following are the contents of the second file:")
print(file2.read())
file1.close()
file2.close()

file1 = open("sample_doc.txt","a+")
file2 = open("Codingal.txt","r")
file1.write(file2.read())
file1.seek(0)
print("The following is the appended file1:")
print(file1.read())

file1.close()
file2.close()