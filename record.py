from dataclasses import dataclass
from dataclasses import field

@dataclass
class Employee:
    id:int
    name: str
    email : str
    phone: str
    department: str

e = Employee(1, "Test", "test@gmail.com", "9876543", "SDWG")

print(e)

@dataclass
class AutoEmployee(Employee):
    empidgenerator = 0
    children: list
    empid: int = field(init=False)

    def __post_init__(self):
        AutoEmployee.empidgenerator += 1
        self.empid = f"{AutoEmployee.empidgenerator}"


a = AutoEmployee(2, "Test2", "test2@gmail.com", "98765432", "SDWG", list(("mal", "tel", "goro")))

b = AutoEmployee(3, "Test2", "test2@gmail.com", "98765432", "SDWG", list(("mal", "tel", "goro")))
print(a)
print(b)