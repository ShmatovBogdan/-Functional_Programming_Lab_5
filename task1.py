# Комплексні числа (Complex)

# Створити ADT-тип (через добуток примітивних типів) для комплексних чисел 
# і реалізувати базову арифметику (додавання, віднімання, добуток, обчислення
# спряженого числа, обчислення модуля комплексного числа).

from math import sqrt

def complex_add(c1, c2):
    match c1, c2:
        case (a1, b1), (a2, b2):
            return (a1 + a2, b1 + b2)

def complex_sub(c1, c2):
    match c1, c2:
        case (a1, b1), (a2, b2):
            return (a1 - a2, b1 - b2)

def complex_mul(c1, c2):
    match c1, c2:
        case (a1, b1), (a2, b2):
            return (a1*a2 - b1*b2, a1*b2 + a2*b1)

def complex_conj(c):
    match c:
        case (a, b):
            return (a, -b)

def complex_abs(c):
    match c:
        case (a, b):
            return sqrt(a**2 + b**2)

if __name__ == "__main__":
    c1 = (3, 4)
    c2 = (1, -2)
    print("Add:", complex_add(c1, c2))
    print("Sub:", complex_sub(c1, c2))
    print("Mul:", complex_mul(c1, c2))
    print("Conj c1:", complex_conj(c1))
    print("Abs c1:", complex_abs(c1))
