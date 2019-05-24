def bisectionMethod(f, left, right, eps=1e-15):
    # if "sign of f(left)" == "sign of f(right)" 
    if not ((f(left)>=0) ^ (f(right)>=0)):
        return "wrong range"
    elif (f(left)==0):
        return left
    elif (f(right)==0):
        return right
    
    while True:
        c = (left + right)/2
        fc = f(c)
        if (abs(left - right)/2 < eps) or (fc == 0):
            return c
        if (fc > 0):
            if (f(left) < 0) and (f(right) > 0):
                right = c
            elif (f(left) > 0) and (f(right) < 0):
                left = c
        else :
            if (f(left) < 0) and (f(right) > 0):
                left = c
            elif (f(left) > 0) and (f(right) < 0):
                right = c


if __name__ == "__main__":
    print(bisectionMethod(lambda x: x**2 - 1, 0, 2))
    print(bisectionMethod(lambda x: x**2 - 1, 0, -2))