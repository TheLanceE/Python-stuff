from pickle import dump,load
"""f=open("test.dat","wb")
x=float(input("donner x"))
dump(x,f)
y=float(input("donner y"))
dump(y,f)
s=x+y
dump(s,f)
f=open("test.dat","rb")
z=load(f)
n=load(f)
s=load(f)
y=load(f)"""
f=open("test.dt","ab")
z=float(input("Donner z"))
dump(z,f)
print(z)
f.close()