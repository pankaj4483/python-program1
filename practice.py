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

my_cat=cat()
my_cat.speak()

print()

class bird(animal):
    def speak(self):
        print("tweet")
my_bird =bird()
my_bird.speak()

print()

class animal:
    def speak(self):
        print("animal sound")
class dog(animal):
    def speak(self):
        super().speak()
        print("woof!")

my_dog=dog()
my_dog.speak()

print()

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
    def introduction(self):
        super().introduction()
        print(f"course:{self.course}")
my_student=student("pankaj",20,"ECE")
my_student.introduction()













    
