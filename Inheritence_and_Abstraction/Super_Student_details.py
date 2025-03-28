class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def disp_person(self):
        print("My name is ",self.fname,self.lname)

class student(person):
    def __init__(self,fname,lname,Gyear):
        self.Gyear = Gyear
        super().__init__(fname,lname)
    
    def disp_student(self):
        self.disp_person()
        print("My graduation year is ",self.Gyear)

s1 = student("Nathaniel","Issac",2011)
s1.disp_student()