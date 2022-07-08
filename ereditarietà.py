class Lista():
  LISTA = []
  NOME= "nome"
  COGNOME= "cognome"
  ETà= 12
  PROFESSIONE= "Lavoro"
 
utente = Lista()   
utente.NOME= input("inserici il nome")
utente.COGNOME= input("inserici il cognome")
utente.ETà= input("inserici l'età")
utente.PROFESSIONE= input("inserici la professione")

if (type(utente.NOME) == str):
    utente.LISTA.append (utente.NOME)
if (type(utente.COGNOME) == str):
    utente.LISTA.append (utente.COGNOME)  
if (int(utente.ETà)):
    utente.LISTA.append (utente.ETà)     
if (type(utente.PROFESSIONE) == str):
    utente.LISTA.append (utente.PROFESSIONE) 
print(utente.LISTA)
