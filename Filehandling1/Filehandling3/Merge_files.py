with open("sample_doc.txt","r") as file1:
    data1 = file1.read()
file1.close()

with open("C.txt","r") as file1:
    data2 = file1.read()
file1.close()

data1 = data1 + "\n \n \n" + data2

with open("NewOne.txt","w") as file1:
    file1.write(data1)
file1.close()

with open("NewOne.txt","r") as file1:
    print(file1.read())
file1.close()