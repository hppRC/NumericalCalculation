def quadraticEquation(a, b, c):
    D = b*b - 4*a*c
    x1 = (-b + D**(0.5))/(2*a)
    x2 = c / (a*x1)

    return (x1, x2)


