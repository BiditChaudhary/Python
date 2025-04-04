file1 = open("sample_doc.txt","r")
file2 = open("C.txt","w")

lines_read_so_far = set()

for line in file1:
    if not(line in lines_read_so_far):
        file2.write(line)

    lines_read_so_far.add(line)

file2.close()
file1.close()