# Вектори 2D (Vector2) і базові операції

# Створити ADT для векторів у 2D (через добуток примітивних типів). 
# Реалізувати операції норми, скалярний, векторний добуток, змішаний добуток.

from __future__ import annotations
from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

def vector_norm(v) -> float:
    match v:
        case Vector2D(x, y):
            return sqrt(x**2 + y**2)

def vector_dot(v1, v2) -> float:
    match v1, v2:
        case (Vector2D(x1, y1), Vector2D(x2, y2)):
            return x1*x2 + y1*y2

def vector_cross(v1, v2) -> float:
    match v1, v2:
        case (Vector2D(x1, y1), Vector2D(x2, y2)):
            return x1*y2 - y1*x2

if __name__ == "__main__":
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    print("Norm v1:", vector_norm(v1))
    print("Dot:", vector_dot(v1, v2))
    print("Cross:", vector_cross(v1, v2))
