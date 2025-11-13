# Матриця 2x2 і лінійні перетворення

# Добуток типів Matrix2. Операції: детермінант, обернена, добуток.

def matrix_det(m):
    match m:
        case ((a, b), (c, d)):
            return a*d - b*c

def matrix_inv(m):
    match m:
        case ((a, b), (c, d)):
            det = a*d - b*c
            if det == 0:
                raise ValueError("Matrix is singular")
            return ((d/det, -b/det), (-c/det, a/det))

def matrix_mul(m1, m2):
    match m1, m2:
        case ((a1, b1), (c1, d1)), ((a2, b2), (c2, d2)):
            return ((a1*a2 + b1*c2, a1*b2 + b1*d2),
                    (c1*a2 + d1*c2, c1*b2 + d1*d2))

if __name__ == "__main__":
    m0 = (1, 2)
    m1 = ((1, 2), (3, 4))
    m2 = ((2, 0), (1, 2))
    print("Det m1:", matrix_det(m1))
    print("Mul m1*m2:", matrix_mul(m1, m2))
    print("Inv m1:", matrix_inv(m1))
