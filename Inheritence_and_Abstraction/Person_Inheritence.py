class person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print("The person ID is",self.id,"And the person's name is",self.name)

class employee(person):
    def __init__(self,id,name,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,id,name)

    def display_employee(self):
        print("The Employee's salary is",self.salary,"And their post is",self.post)
        person.display(self)

emp1 = employee(101,"Nathan",6000,"Secretary")
emp1.display_employee()
    