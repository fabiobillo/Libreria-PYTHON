class Person:
    def __init__(self,fnome,lnome):
      self.firstnome=fnome
      self.lastnome=lnome

    def printnome(self):
     print(self.firstnome, self.lastnome)

class Student(Person):
    def __init__(self,fnome,lnome,matricola):
      Person.__init__(self,fnome,lnome)
      self.NumMatr=matricola  
    def printnome(self):
     print(self.firstnome, self.lastnome,self.NumMatr)  

class Professor(Student):
    def __init__(self,fnome,lnome,matricola,materia):
      Student.__init__(self,fnome,lnome,matricola)
      self.MateriaProf=materia
    def printnome(self):
     print(self.firstnome, self.lastnome,self.NumMatr,self.MateriaProf)

ListaPerson=[]
ListaStudent=[]
ListaProfessor=[]

i=1
while i<3:
  
    TipoUtente= input ("inserisci se sei Person, Student o Professor")

    if TipoUtente=="Person":
        fnome=input("inserisci il nome")
        lnome=input("inserisci il cognome")
        x= Person(fnome,lnome)
        x.printnome()
        ListaPerson.append(x.firstnome)
        ListaPerson.append(x.lastnome)
        print (ListaPerson)
        ContPerson=len(ListaPerson)/2
        print(ContPerson)
    elif TipoUtente=="Student":
        fnome=input("inserisci il nome")
        lnome=input("inserisci il cognome")
        matricola=input("inserisci la matricola")
        y= Student(fnome,lnome,matricola)
        y.printnome()
        ListaStudent.append(y.firstnome)
        ListaStudent.append(y.lastnome)
        ListaStudent.append(y.NumMatr)
        ContStudent=len(ListaStudent)/3
        print(ContStudent)
    elif TipoUtente=="Professor":
        fnome=input("inserisci il nome")
        lnome=input("inserisci il cognome")
        matricola=input("inserisci la matricola")
        materia=input("inserisci la materia")
        print(ListaStudent)
        z= Professor(fnome,lnome,matricola,materia)
        z.printnome()
        ListaProfessor.append(z.firstnome)
        ListaProfessor.append(z.lastnome)
        ListaProfessor.append(z.NumMatr)
        ListaProfessor.append(z.MateriaProf)
        print(ListaProfessor)
        ContProfessor=len(ListaProfessor)/4
        print(ContProfessor)

    i = i + 1
    print(i)

    
  



