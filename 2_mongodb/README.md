# MongoDB

### Užduoties formuluotė
>Sumodeliuokite duomenų bazę tinkama dokumentų modeliui (modelį pateikite grafiniu formatu).  Parašykite programą, kuri atlieka operacijas pagal reikalavimus.

>Dalykinėje srityje turi būti bent 3 esybės. Sumodeliuokite bent dvi atskirose kolekcijose, bent dvi esybės turinčios kompozicijos sąryšį turi būti modeliuojamos tame pačiame dokumente (angl. embedded).

>Parašykite užklausas:

>1) Įdėtinėms (angl. embedded) esybėms gauti (banko pavyzdžiu - visas, visų klientų sąskaitas).

>2) Bent vieną agreguojančią užklausą (banko pavyzdžiu - visų klientų balansus)

>3) Parašykite tą pačią agreguojančią užklausą (kaip ir #2 punkte) su map-reduce

## Duomenų bazės modelis
Pasirinkta dalykinė sritis - kurjerių paslaugos. Duomenų bazę sudaro 6 esybės. Jose saugoma informacija ir tarpusavio sąryšis pateikiamas diagramoje.

![Duomenų bazės diagrama](db_diagrama.png)

Sukuriamos 3 kolekcijos: *routes*, *couriers*, *shipments*.
* **routes** kolekcija apjungia maršrutų ir vietovių lenteles;
* **couriers** kolekcija saugo kurjerių duomenis;
* **shipments** kolekcija saugo siuntų, siuntėjų, gavėjų ir adresų duomenis.

Dokumentų pavyzdžiai saugomi JSON failuose `couriers`, `routes` ir `shipments` kataloguose.

## Užklausos

1. Iš *shipments* kolekcijos nuskaitomi visų siuntų siuntėjų adresai

Funkcija:
```
def findNames():
    for x in shipments.find():
        print(x["siuntėjas"]["adresas"])
```
Rezultatas:
```
{'miestas': 'Vilnius', 'gatvė': 'Didlaukio', 'namoNr': '47', 'butoNr': None}
{'miestas': 'Vilnius', 'gatvė': 'Ateities', 'namoNr': '15', 'butoNr': None}
{'miestas': 'Vilnius', 'gatvė': 'Geležinio Vilko', 'namoNr': '30', 'butoNr': None}
{'miestas': 'Vilnius', 'gatvė': 'Ukmergės', 'namoNr': '47', 'butoNr': None}
{'miestas': 'Kaunas', 'gatvė': 'Vilniaus', 'namoNr': '47', 'butoNr': None}
```

2. Randamas kiekvieno maršruto bendras siuntų svoris

Funkcija:
```
def findShipmentWeight():
    ships = shipments.aggregate([
        { "$group":{ "_id":"$maršrutoID", "bendras_svoris":{"$sum":"$svoris"} } },
        { "$sort":{ "bendras_svoris":-1 } }
    ])
    for x in ships:
        print(x)
```
Rezultatas:
```
{'_id': ObjectId('6370a77747c8161ffcbe403f'), 'bendras_svoris': 10.5}
{'_id': ObjectId('6370a77747c8161ffcbe4040'), 'bendras_svoris': 9.8}
```

3. 2 užklausa atliekama su Map Reduce

Funkcija:
```
def findShipmentWeightMapReduce():
    map_func = Code('function() { emit( this["maršrutoID"], this["svoris"] ); }')
    reduce_func = Code('function(key, values) { return Array.sum(values); }')

    database.command(
        'mapReduce',
        'shipments',
        map = map_func,
        reduce = reduce_func,
        out = "shipment_weight"
    )

    for x in database.shipment_weight.find():
        print(x)
```
Rezultatas:
```
{'_id': ObjectId('6370a77747c8161ffcbe403f'), 'value': 10.5}
{'_id': ObjectId('6370a77747c8161ffcbe4040'), 'value': 9.8}
```