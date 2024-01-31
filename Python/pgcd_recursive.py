def pgcd(x,y):
    if x=y:
        return x
    elif x>y:
        return pgcd(x-y,y)
    else:
        return pgcd(x,y-x)
    