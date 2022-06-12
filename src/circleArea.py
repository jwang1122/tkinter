from math import pi

def circleArea(radius):
    return pi * radius**2

if __name__ == '__main__':
    r = 1
    a = circleArea(r)
    print(f"the circle area with radius={r} is {a:.3f}.")