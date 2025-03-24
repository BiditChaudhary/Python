class parrot:
    Species = "Gray parrot"

    def __init__(self,name1,age1):
        self.name1 = name1
        self.age1 = age1

    def display(self):
        print("My name is {0} My age is {1}".format(self.name1,self.age1))

p1 = parrot("Tsipora",3)
p1.display()
print("The species is",p1.Species)