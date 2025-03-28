from abc import ABC, abstractmethod
class animal:
    @abstractmethod
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I am a human and I move by walking.")

class snake(animal):
    def move(self):
        print("I a ma snake and I move by crawling.")

class fish(animal):
    def move(self):
        print("I am a fish and I move by swimming.")

f1 = fish()
h1 = human()
s1 = snake()
for i in [f1,h1,s1]:
    i.move()