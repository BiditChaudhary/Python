with open("sample_doc.txt","w") as file:
    file.write("The Lord is my shepherd...")
file.close()

with open("Codingal.txt","r") as file:
    cont = file.readlines()
    for i in cont:
        print(i.split())

file.close()