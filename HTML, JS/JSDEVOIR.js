function verif(){
    //recupération;entr=Entrée ID;pp=Plat Principale ID;dssr=Dessert ID;
    a=document.getElementById('cin').value
    b=document.getElementById('np').value
    entr=document.getElementById('entr').selectedIndex
    pp=document.getElementById('pp').selectedIndex
    dssr=document.getElementById('dssr').selectedIndex
    r1=document.getElementById('r1').checked
    r2=document.getElementById('r2').checked
    //conditions
    if ((!r1) && (!r2)){alert('la selection du genre est obligatoire');return false}
    if (a.length!=8){alert('le Cin est incorrecte!');return false}
    if (b.length>20){alert('nom et prenom sont plus que 20 caractères!');return false}
    if((entr==0)||(pp==0)||(dssr==0)){alert('Le choix du menu est obligatoire');return false}
    //client fidèle ; cb=checkbox ID;txta=text area ID;
    if (document.getElementById('cb').checked){document.getElementById('txta').innerHTML="Mr/Mme nomprenom \n Merci pour votre visite \n Vous bénéficiez d'une réduction de 20%"}
    else {document.getElementById('txta').innerHTML="Mr/Mme nomprenom \n Merci pour votre visite \n Vous bénéficiez d'une réduction de 5%"}
}