def gaussianElimination(A, y=None):
    N = len(A)
    if (y!=None):
        for i in range(N):
            A[i].append(y[i])

    for k in range(N-1):
        aiks = [A[i][k] for i in range(k,N)]
        aiks = list(map(abs, aiks))
        l = aiks.index(max(aiks))
        if (k != k+l):
            tmpa = [i for i in A[k]]
            for i in range(k,N+1):
                A[k][i] = A[k+l][i]
                A[k+l][i] = tmpa[i]

        for i in range(k+1, N):

            alpha = A[i][k] / A[k][k]
            for j in range(N+1):
                A[i][j] -= alpha * A[k][j]

    x = [0 for i in range(N)]
    x[N-1] = A[N-1][N] / A[N-1][N-1]

    for i in range(N-2, -1, -1):
        x[i] = (A[i][N] - sum([A[i][k]*x[k] for k in range(i+1, N)])) / A[i][i]

    return x

if __name__ == "__main__":
    A = [[1, -1, 2, 4],
         [2, -2, 1, 2],
         [-1, 3, 1, 8]]
    print(gaussianElimination(A))

    A = [[1, -1, 2],
         [2, -2, 1],
         [-1, 3, 1]]
    y = [4, 2, 8]
    print(gaussianElimination(A, y))