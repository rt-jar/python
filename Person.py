class Person:
   def __init__(self, name, age):
    self.name=name
    self.age=age

   def __str__(self):
     return f"{self.name} is of age {self.age}"

p=Person("Rakesh", 25)

print(p)