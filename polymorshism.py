# polymorphism in action-loop
class dog:
    def speak(self):
        print("woof")

class cat:
    def speak(self):
        print("meow")

animals=[dog(), cat()]

for animal in animals:
    animal.speak()
