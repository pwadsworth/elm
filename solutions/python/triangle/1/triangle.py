from functools import reduce

def equilateral(sides):
    return isValid(sides) and len(set(sides)) == 1


def isosceles(sides):
    return isValid(sides) and len(set(sides)) < 3


def scalene(sides):
    return isValid(sides) and len(set(sides)) == 3
    

def isValid(sides:list[int]): 
    a, b, c = sides
    return a+b >= c and b + c >= a and a + c >= b