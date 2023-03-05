function CONTROL_SAISIE() {
  ch = document.getElementById("b1").value;
  ch1 = document.getElementById("b2").value;
  v3=document.getElementById("b3").selectedIndex;
  
  if (ch.length != 3 || isNaN(ch)) {
    alert("code est un entier de trois chiffres");
  }
  if(v3==0){alert(" selection obligatoire");return false;}
  if (ch1.length == 0) {
    alert("veuillez ecrire votre nom et prenom");
  }
  note=0;
	if(document.getElementById('b5').checked){note++;}
	if(document.getElementById('b6').selectedIndex==2){note++;}
	if((document.getElementById('b7').checked==false)&&
		(document.getElementById('b8').checked==true)&&
		(document.getElementById('b9').checked==true)&&
		(document.getElementById('b10').checked==true))
		{note++;}

  alert(ch1+" votre note est " + note);
}
