IP=input("Donner une adresse IP : ")
IP1=IP[0:IP.find(".")]
if IP1 in [1,127]:
    print (IP," est de Classe A car",IP1," € [1 .. 127]")
elif IP1 in [128 ..191]:
    print (IP," est de Classe B car",IP1," € [128 .. 191]")
elif IP1 in [192..223]:
    print (IP," est de Classe C car",IP1," € [192 .. 223]")
