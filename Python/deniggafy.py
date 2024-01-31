from pickle import dump,load
def saisir():
    n=int(input("n="))
    while not 2<=n<=10:
        n=int(input("n="))
    return n
def verif(r):
    v=True
    i=0
    while v and i<len(r) :
        if "A"<=r[i]<="Z" :
            i=i+1
        else:
            v=False
    return v
def remp1():
    f=open("question.txt","w")
    ch=""
    for i in range (n):
        q=str(input("question="))
        while not((len(q)>=4) and "A"<=q[0]<="Z"):
            q=str(input("question="))
        r=str(input("Reponse="))
        while not verif(r):
            r=str(input("Reponse="))
        if r=="VRAI":
            ch=q+"#"+r
        elif r=="FAUX":
            ch=q+"#"+r
        else:
            r=str(input("Reponse="))
        f.write(ch+"\n")
    f.close()
def remp2():
    f=open("score.dat","wb")
    
    
n=saisir()
remp1()
remp2()
