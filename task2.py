# Вектори 2D (Vector2) і базові операції

# Створити ADT для векторів у 2D (через добуток примітивних типів). 
# Реалізувати операції норми, скалярний, векторний добуток, змішаний добуток.

from math import sqrt

def vector_norm(v):
    match v:
        case (x, y):
            return sqrt(x**2 + y**2)

def vector_dot(v1, v2):
    match v1, v2:
        case (x1, y1), (x2, y2):
            return x1*x2 + y1*y2

def vector_cross(v1, v2):
    match v1, v2:
        case (x1, y1), (x2, y2):
            return x1*y2 - y1*x2

if __name__ == "__main__":
    v1 = (1, 2)
    v2 = (3, 4)
    print("Norm v1:", vector_norm(v1))
    print("Dot:", vector_dot(v1, v2))
    print("Cross:", vector_cross(v1, v2))
