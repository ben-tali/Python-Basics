# class definition
class SoftwareEngeneer:
  # constructors
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
#methods and properties

    def sayHello(self):
        print(f"{self.name} is saying hello to you")


se1 = SoftwareEngeneer("Baraka", 45, "Junior", "5000")

print(se1.name)

se1.sayHello()

# inheritance


class Coder(SoftwareEngeneer):

    def __init__(self, name, age, level, salary, task):
        super().__init__(name, age, level, salary)
        self.task = task

    def start_task(self):
        print(f"{self.name} has started doing {self.task}")


max = Coder("max", 45, "senior", 5000, "Writting code")

max.sayHello()
max.start_task()
