import json
import pickle
import pprint

a={
    "a":11,
    "b":24,
    "c":11
}
print(a)

B="siamo la classe migliore di"

print(B)

print("che tipo di conversione vuoi fare?")
scelta_conv= input("1.Pickle - 2.Json")
pyt= pickle
jsn= json
convertitore=""
if scelta_conv=="1":
    convertitore=pyt
elif scelta_conv=="2":
    convertitore=jsn

#cambia c
y=convertitore.dumps(a)
z=convertitore.loads(y)
z["c"] = input("modifica parametro c")  
print(z)

#aggiungi parola

t=convertitore.dumps(B)
v=convertitore.loads(t)
v = v + " " + input("aggiungi una frase") 
print(v)




"""
data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print ('DATI:')
pprint.pprint(data)
data_string = pickle.dumps(data)
print ('PICKLE:')
print(data)
r = data_string
# data_string = open ("file.txt","rb" )
data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]    # pos 123
data1_string = pickle.dumps(data1)
data2 = pickle.loads(data1_string)    # pos 125
print ("DOPO:")
pprint.pprint(data2)
print ("STESSI?:")
print (data1 is data2)
print ("UGUALI?:")
print (data1 == data2)
"""