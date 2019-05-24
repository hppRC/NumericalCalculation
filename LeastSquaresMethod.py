def leastSquaresMethod(x, y):
    N = len(x)
    a1 = N*sum([xi*yi for xi, yi in zip(x, y)]) - sum(x)*sum(y)
    a2 = N*sum([xi*xi for xi in x]) - (sum(x))**2

    b1 = sum([xi*xi for xi in x])*sum(y) - sum(x)*sum([xi*yi for xi, yi in zip(x, y)])
    b2 = a2

    A = a1/a2
    B = b1/b2

    return lambda x: A*x + B


if __name__ == "__main__":
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    print(leastSquaresMethod(x,y)(1.5))