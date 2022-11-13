# MongoDB

Siuntų pristatymo paslaugos.

### Duomenų bazės struktūros diagrama
![Duomenų bazės diagrama](db_diagrama.png)

Sukuriamos 3 kolekcijos: *routes*, *couriers*, *shipments*.
* **routes** kolekcija apjungia maršrutų ir vietovių lenteles;
* **couriers** kolekcija saugo kurjerių duomenis;
* **shipments** kolekcija saugo siuntų, siuntėjų, gavėjų ir adresų duomenis.

### Užklausos

1. Iš *shipments* kolekcijos nuskaitomi visų siuntų siuntėjų adresai

2. Randamas kiekvieno maršruto bendras siuntų svoris

3. 2 užklausa atliekama su Map Reduce