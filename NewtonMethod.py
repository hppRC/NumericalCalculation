def newtonMethod(f, df, x, eps=1e-5):
    while True:
        new_x = x - f(x)/df(x)
        if (abs(new_x - x) < eps*abs(new_x)):
            return new_x
        x = new_x


if __name__ == "__main__":
    print(newtonMethod(lambda x: x*x, lambda x: 2*x, 1))
