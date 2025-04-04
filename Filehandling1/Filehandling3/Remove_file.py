import os

if os.path.exists("Text.txt"):
    os.remove("Text.txt")
else:
    MyFile2 = open("sample_doc.txt","w")
    MyFile2.write("The new file.")
    MyFile2.close()

os.remove("FolderToBeRemoved")