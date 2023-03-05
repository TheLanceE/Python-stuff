x=int(input("Donner un entier X : "))
ch=str(x)
n=len(ch)
y=x**2
v=str(y)
D=int(v[len(v)-n:len(v)])
G=int(v[0:len(v)-n])
if D+G==x:
    print(x," est un nombre Kaprékar.")
else:
    print(x," n'est pas un nombre Kaprékar.")
