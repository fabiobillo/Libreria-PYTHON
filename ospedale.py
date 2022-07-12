
from multiprocessing.sharedctypes import Value
from optparse import Values


class ospedale:
    def __init__(self,ore):
      self.Totore=ore
    def printbudget(self):
     print(self.Totore)
    def PagaOreDott():
        print(dizDott)
        Dott=str(input("chi vuoi pagare?"))
        dizDott.pop(Dott)
        print(dizDott)
    def PagaOreSpec():
        print(dizDott)
        Spec=str(input("chi vuoi pagare?"))
        dizSpec.pop(Spec)
        print(dizSpec)

class dottore(ospedale):
    def __init__(self,ore,nome):
      ospedale.__init__(self,ore) 
      self.id=nome 
    def printbudget(self):
      print(self.Totore)
    

class specialisti_dottore(dottore):
    def __init__(self,ore,nome):
      dottore.__init__(self,ore,nome)
    def printbudget(self):
      print(self.Totore) 

ListaOreDottore=[]
ListaOreSpecialista=[]
dizDott={}
dizSpec={}

  
TipoUtente= input ("inserisci 1 se sei dottore o 2 se sei specialista")

if TipoUtente=="1":
    nome=input("inserisci il nome")
    ore=int(input("inserisci le ore lavorate"))
    x= dottore(nome,ore)
    ListaOreDottore.append(ore)
    dizDott.update({nome:ore})
   
    ospedale.PagaOreDott()
    

elif TipoUtente=="2":
     nome=input("inserisci il nome")
     ore=int(input("inserisci le ore lavorate"))
     x= specialisti_dottore(nome,ore)
     ListaOreSpecialista.append(ore)
     dizSpec.update({nome:ore})
    
     ospedale.PagaOreSpec()
     


"""
budgetComune=float(input("inserisci il budget da suddividere"))
budget=float(budgetComune*0.4)
x=comune(budget)
x.printbudget()
budget=float(budgetComune*0.3)
y=asl(budget)
y.printbudget()
budget=float(budgetComune*0.3)
z=proloco(budget)
z.printbudget()
"""
