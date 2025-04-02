file = open("codingal.txt","r")
file2 = open("sample_doc.txt","w")
cont = file.readlines()

for lines in range(1,len(cont)):
    if lines % 2 != 0:
        file2.write(cont[lines-1])

file.close()
file2.close()

file2 = open("sample_doc.txt","r")
print(file2.read())
file2.close()