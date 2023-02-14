ch=input("Donner une expression arithmétique : ")
#
x=0
op=ch[0]
ch1=int(ch[1:ch.find(" ")])
ch2=int(ch[ch.find(" ")+1:])
#
if op=="+":
    x=ch1+ch2
elif op=="-":
    x=ch1-ch2
elif op=="*":
    x=ch1*ch2
elif op=="/":
    x=ch1/ch2
#
print(ch1,op,ch2,"=",x)