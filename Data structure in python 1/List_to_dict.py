def test(first):
    Result = {}
    for item in first:
        Result[item[0]] = item[1:]
    print(Result)



student = [[1, "Jean Castro","VIII"],[2,"Daniel Issac","VII"],[3, "Mercy Issac","V"],[4,"Omer Adoni","X"]]
print(student)
test(student)