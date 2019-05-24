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


if __name__ == "__main__":
    xs = [i for i in range(-5, 6)]
    ys = [1/(1 + 25*i*i) for i in range(-5, 6)]
    dots = [lagrangeInterpolation(i*0.1, xs, ys) for i in range(-5, 6)]
    print(dots)
