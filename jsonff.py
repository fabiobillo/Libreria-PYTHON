import json

listaCandidati=[]

scelta_json=""
while scelta_json!="end":
    print("che vosa vuoi fare?")
    print("1. Caricare")
    print("2. visualizzare")
    print("end per uscire")
    scelta_json=input("")
    if scelta_json=="1":

        scelta="si"
        while scelta=="si":
            nome=input("inserisci il nome del candidato")
            listaCandidati.append(nome)
            print(listaCandidati)
            if len(listaCandidati) >0:
                y=json.dumps(listaCandidati)
                scelta= input("vuoi inserire altri candiadati? si/no")
            else:
                print("non hai inserito dati")    
                scelta= input("vuoi provare ad inserire altri candiadati con valori corretti? si/no")
    elif scelta_json=="2":
        print("questi sono i candidati:")
        print(listaCandidati)
        scelta="si"
        while scelta=="si":
            if len(listaCandidati) >0:
                y=json.dumps(listaCandidati)
                z=json.loads(y)
                scelta_visualizzazione= int(input("quale candidato vuoi visualizzare? inserisci l'indice"))
                print(z[scelta_visualizzazione - 1])    
                scelta= input("vuoi vissualizzare altri candiadati? si/no")
            else:
                print("non hai inserito dati")    
                scelta= input("vuoi provare ad inserire altri candiadati con valori corretti? si/no")

