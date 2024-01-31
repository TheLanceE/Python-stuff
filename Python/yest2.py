#nt=dict()
"""
nt["ndc1"]=float(input("Donner note de controle 1:"))
nt["ndc2"]=float(input("Donner note de controle 2:"))
nt["nds"]=float(input("Donner note de synthese:"))
"""
e=dict()
e["nom"]=input("Nom : ")
e["prenom"]=input("Prenom : ")
#e["note"]=nt
e["note"]=dict()
e["note"]["ndc1"]=float(input("Donner note de controle 1:"))
e["note"]["ndc2"]=float(input("Donner note de controle 2:"))
e["note"]["nds"]=float(input("Donner note de synthese:"))
e["moy"]=(e["note"]["ndc1"]+e["note"]["ndc2"]+(e["note"]["nds"]*2))/4
#print(nt)
print(e)