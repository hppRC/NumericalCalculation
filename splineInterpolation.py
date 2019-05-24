#x is number list which is provided
#y is number list which is provided
#var is number list which you want to plot
#this function return float number list which is interpolated based on var

def splineInterpolation(var, x, y):
    j = 0
    N = len(x)-1
    a,b,c,d = splineInterpolationCalc(x,y)
    result= []
    for va in var:
        if (j < N-1):
            if(x[j+1] <= va):
                j += 1
        if (x[0]>va or x[N]<va):
            continue
        Sxj = a[j]*((va-x[j])**3) + b[j]*((va-x[j])**2) + c[j]*(va-x[j]) + d[j]
        result.append(Sxj)
    
    return result

def splineInterpolationCalc(x, y):
    N = len(x)-1
    u = [0 for i in range(N+1)]

    h = [x[i+1]-x[i] for i in range(N)]
    v = [6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1]) for i in range(1, N)]

    d = [0 for i in range(N+1)]
    l = [0 for i in range(N+1)]
    z = [0 for i in range(N+1)]

    d[0] = 2*(h[0] + h[1])

    for i in range(1, N):
        l[i] = h[i] / d[i-1]
        d[i] = 2*(h[i-1]+h[i]) - l[i]*h[i-1]

    z[0] = v[0]

    for i in range(1, N):
        z[i] = v[i-1] - l[i]*z[i-1]

    u[N-1] = z[N-1]/d[N-1]

    for i in list(range(1, N-1))[::-1]:
        u[i] = (z[i] - h[i]*u[i+1]) / d[i]

    a = [(u[i+1]-u[i])/(6*(x[i+1]-x[i])) for i in range(N)]
    b = [ui/2 for ui in u]
    c = [(y[i+1]-y[i])/(x[i+1]-x[i]) - (x[i+1]-x[i])*(2*u[i]+u[i+1])/6 for i in range(N)]
    d = [y[i] for i in range(N)]

    return (a, b, c, d)


