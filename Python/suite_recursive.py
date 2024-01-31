def U(n):
    if n==0:
        return 2
    elif n=1:
        return 3
    else:
        return (U(n-1)+2*U(n-2))