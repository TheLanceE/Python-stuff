from PyQt5.uic import*
from  PyQt5.QtWidgets import *
from pickle import *

def ajouter():
    F=open("classe.dat","ab")
    e={}
    e["num"]=fen.num.text()
    e["nom"]=fen.nom.text()
    e["classe"]=fen.classe.currentText()
    if fen.h.isChecked():
        e["genre"]="homme"
    elif fen.f.isChecked():
        e["genre"]="femme"
    else:
        e["genre"]=""
    if  e["num"]=="" or e["nom"]=="" or e["genre"]=="":
        QMessageBox.critical(fen,"erreur","veuillez saisiez tout les information!!")
    elif not (len(e["num"])==8 and e["num"].isdigit()):
        QMessageBox.critical(fen,"erreur","veuillez saisiez tout les information!!")
    else:
        QMessageBox.information(fen,"Bravoo","Good Job!")
        dump(e,F)
    print(e)
    F.close()
    

app=QApplication([])
fen=loadUi ('tp1.ui')
fen.show()
fen.add.clicked.connect(ajouter)
app.exec_()