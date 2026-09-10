class animal:
    def speak(self):
        print("animal sound")

class dog(animal):
    def speak(self):
        print("woof")

my_dog=dog()
my_dog.speak()

class cat(animal):
    def speak(self):
        print("meow")


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduction(self):
        print(f"name:{self.name},age:{self.age}")

class student(person):
    def __init__(self,name,age,course):
        super(). __init__(name,age)
        self.name=name
        self.age=age
        self.course=course
        self.pet=None
    def introduction(self):
        super().introduction()
        print(f"course:{self.course}")

    def register_pet(self,pet):
        self.pet=pet
        print(f"{self.name} register his pet")

    def show_pet(self):
        if self.pet is None:
            print("there is no pet register!")
        else:
            self.pet.speak()
#-----test code-----
s1=student("pankaj",20,"ECE")
s1.introduction()

print()
s1.show_pet()

print()
my_pet=dog()
s1.register_pet(my_pet)
s1.show_pet()
