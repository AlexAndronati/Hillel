import pytest

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        if not isinstance(name, str) or not isinstance(age, int) or not isinstance(salary, (int, float)):
            raise ValueError

    def __str__(self):
        return f"{self.__class__.__name__}; dict={self.__dict__}"

    def get_year_salary(self):
        return self.salary*12

    def get_real_salary(self):
        return self.salary*0.95

    def salary_increase(self, a):
        if not isinstance(a, (int, float)):
            raise ValueError
        if a < 0:
            raise ValueError
        self.salary = self.salary + a


def test_get_year_salary():
    p = Person("John", 37, 10000)
    assert p.get_year_salary() == 120_000


def test_get_real_salary():
    p = Person("John", 37, 10000)
    assert p.get_real_salary() == p.salary*0.95


def test_construct():
    with pytest.raises(ValueError):
        Person("John", "37fsdfsdf", 10000)

    with pytest.raises(ValueError):
        Person(5, 37, 10000)

    with pytest.raises(ValueError):
        Person(5, 37, "salary")


def test_salary_increase():
    p = Person("John", 37, 10000)
    p.salary_increase(1000)
    assert p.salary == 11000


def test_salary_increase_error():
    with pytest.raises(ValueError):
        p = Person("John", 37, 10000)
        p.salary_increase("ttttt")

