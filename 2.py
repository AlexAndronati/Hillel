
def init(self, name, age):
    self.name = name
    self.age = age


def grow(self, increment):
    self.age += increment


name = "Person"
bases = object,
attrs = {
    "__init__": init,
    "grow": grow,
    "attr": 33

}

Person = type(name, bases, attrs)
print(Person)
p = Person("John", 7)
print(p.name)
print(p.__dict__)
p.grow(5)
print(p.__dict__)

print(p.attr)
print(Person.attr)
