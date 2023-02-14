N=int(input("Donner un entier de 4 chiffres : "))
N1=N%10
Nc=str(N)
X=int(Nc[3]+Nc[2]+Nc[1]+Nc[0])
if (N*N1)==X :
    print(N," est propre")
else:
    print(N,"n'est pas propre")