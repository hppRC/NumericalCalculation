def lagrangeInterpolation(x, xs, ys) :
    ls = []
    for xj in xs :
        numerator = 1
        denumerator = 1

        for xi in xs:
            if (xi == xj) :
                continue
            else :
                numerator *= x - xi 
                denumerator *= xj - xi 
        ls.append(numerator/denumerator)
    return sum([li * yi for li, yi in zip(ls, ys)])