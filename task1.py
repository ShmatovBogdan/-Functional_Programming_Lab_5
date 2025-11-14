# Комплексні числа (Complex)

# Створити ADT-тип (через добуток примітивних типів) для комплексних чисел 
# і реалізувати базову арифметику (додавання, віднімання, добуток, обчислення
# спряженого числа, обчислення модуля комплексного числа).

from __future__ import annotations
from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Complex:
    a: float
    b: float

def complex_add(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case (Complex(a1, b1), Complex(a2, b2)):
            return Complex(a1 + a2, b1 + b2)

def complex_sub(c1, c2) -> Complex:
    match c1, c2:
        case (Complex(a1, b1), Complex(a2, b2)):
            return Complex(a1 - a2, b1 - b2)

def complex_mul(c1, c2) -> Complex:
    match c1, c2:
        case (Complex(a1, b1), Complex(a2, b2)):
            return Complex(a1*a2 - b1*b2, a1*b2 + a2*b1)

def complex_conj(c) -> Complex:
    match c:
        case Complex(a, b):
            return Complex(a, -b)

def complex_abs(c) -> float:
    match c:
        case Complex(a, b):
            return sqrt(a**2 + b**2)

if __name__ == "__main__":
    c1 = Complex(3, 4)
    c2 = Complex(1, -2)
    print("Add:", complex_add(c1, c2))
    print("Sub:", complex_sub(c1, c2))
    print("Mul:", complex_mul(c1, c2))
    print("Conj c1:", complex_conj(c1))
    print("Abs c1:", complex_abs(c1))
