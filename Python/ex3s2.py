D="1"
for N in range(100,999):
    for i in range(100,999):
        if (N%i)==0:
            D=D+"+"+str(i)            
            print(D)