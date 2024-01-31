def pui(a,n):
    if n==0:
        return 1
    else:
        return a*pui(a,n-1)
print(pui(4,4))

    