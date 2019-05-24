# x is number to get y (is interpolated)
# xs is number list which is provided
# ys is number list which is provided

def lagrangeInterpolation(va, x, y) :
    ls = []
    for xj in x :
        numerator = 1
        denumerator = 1

        for xi in x:
            if (xi == xj) :
                continue
            else :
                numerator *= va - xi 
                denumerator *= xj - xi 
        ls.append(numerator/denumerator)
    return sum([li * yi for li, yi in zip(ls, y)])


if __name__ == "__main__":
    x = [i for i in range(-5, 6)]
    y = [1/(1 + 25*i*i) for i in range(-5, 6)]
    dots = [lagrangeInterpolation(i*0.1, x, y) for i in range(-5, 6)]
    print(dots)
