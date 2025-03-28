class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}, I am a dog, my age is {self.age}.")

    def sound(self):
        print("I make sound by barking.")

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}, I am a cat, my age is {self.age}.")
    
    def sound(self):
        print("I make sound by meowing.")


d1 = dog("Danny Dog",3)
c1 = cat("Kitty",2)
for animal in [d1,c1]:
    animal.info()
    animal.sound()
    