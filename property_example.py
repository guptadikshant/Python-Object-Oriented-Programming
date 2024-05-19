class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # converts a method into an attribute
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name: str):
        first, last = name.split(" ")
        self.first = first
        self.last = last


if __name__ == "__main__":
    emp1 = Employee("John", "Smith")
    emp1.full_name = "Jim None"
    print(emp1.first)
    print(emp1.last)
    print(emp1.email)
    print(emp1.full_name)
