

class EMailException(Exception):
    def __init__(self, text):
        print(text)


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if value[0] != "@" and value.endswith("@gmail.com"):
            instance._email = value
        else:
            raise EMailException("Wrong E-Mail")


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()

my_class.email = "validemail@gmail.com"
print(my_class.email)

my_class.email = "novalidemail"
print(my_class.email)
print(my_class.__dict__)

