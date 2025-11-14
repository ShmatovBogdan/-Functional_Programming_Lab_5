# Матриця 2x2 і лінійні перетворення 
# Добуток типів Matrix2. Операції: детермінант, обернена, добуток.

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Matrix2x2:
    a1: float
    a2: float
    b1: float
    b2: float

def matrix_det(m: Matrix2x2) -> float:
    match m:
        case Matrix2x2(a1=a1, a2=a2, b1=b1, b2=b2):
            return a1 * b2 - a2 * b1

def matrix_inv(m: Matrix2x2) -> Matrix2x2:
    match m:
        case Matrix2x2(a1=a1, a2=a2, b1=b1, b2=b2):
            det = a1 * b2 - a2 * b1
            if det == 0:
                raise ValueError("Matrix is singular")
            return Matrix2x2(
                a1=b2/det,
                a2=-a2/det,
                b1=-b1/det,
                b2=a1/det
            )

def matrix_mul(m1: Matrix2x2, m2: Matrix2x2) -> Matrix2x2:
    match m1, m2:
        case (Matrix2x2(a1=a1, a2=a2, b1=b1, b2=b2),
              Matrix2x2(a1=c1, a2=c2, b1=d1, b2=d2)):
            return Matrix2x2(
                a1=a1*c1 + a2*d1,
                a2=a1*c2 + a2*d2,
                b1=b1*c1 + b2*d1,
                b2=b1*c2 + b2*d2
            )

if __name__ == "__main__":
    m1 = Matrix2x2(1, 2, 3, 4)
    m2 = Matrix2x2(2, 0, 1, 2)
    print("Det m1:", matrix_det(m1))
    print("Mul m1*m2:", matrix_mul(m1, m2))
    print("Inv m1:", matrix_inv(m1))
