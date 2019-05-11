# x is number to get y (is interpolated)
# xs is number list which is provided
# ys is number list which is provided

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