

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.__class__.__name__}; dict={self.__dict__}"


class Manager(Person):
    def __init__(self, age, name, salary, department):
        super().__init__(age, name, salary)
        self.department = department


if __name__ == '__main__':
    person = Person("Morty", 8, 10)
    manager = Manager("Rick", 60, 10000, "1ABC")
    print(person)
    print(manager)

