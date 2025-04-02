Myfile = open("sample_doc.txt","r")
file2 = open("Newfile.txt","w")

for lines in Myfile.readlines():
    if not(lines.startswith("Coding")):
        print(lines)
        file2.write(lines)

Myfile.close()
file2.close()