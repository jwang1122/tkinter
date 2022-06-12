from math import pi

class Student:
    def __init__(self, name, id, age, gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

    def calculateCircleArea(self, radius):
        return pi*radius**2

if __name__ == '__main__':
    s = Student("Bob", "S-123", 13, 'M')
    r = 2
    a = s.calculateCircleArea(r)
    print(f"the circle area with radius={r} is {a:.3f}.")

