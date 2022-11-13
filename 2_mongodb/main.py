import pymongo
import json
import codecs
from bson import Code

# duomenu baze
client = pymongo.MongoClient(host="localhost", port=27017)
database = client.courier_service

# kolekcijos
routes = database.routes
couriers = database.couriers
shipments = database.shipments

# ------------------- DOKUMENTŲ KŪRIMAS -------------------

# iš failų nuskaitomi ir į duombazę pridedami maršrutai
def addRoutes(n):
    for i in range(n):
        with codecs.open('routes/route'+str(i+1)+'.json', encoding="utf-8") as json_file:
            route = json.load(json_file)
            routes.insert_one(route)

# iš failų nuskaitomi ir į duombazę pridedami kurjeriai
def addCouriers(n):
    for i in range(n):
        with codecs.open('couriers/courier'+str(i+1)+'.json', encoding="utf-8") as json_file:
            courier = json.load(json_file)
            courier["maršrutoID"] = routes.find()[i]["_id"]
            couriers.insert_one(courier)

# iš failų nuskaitomos ir į duombazę pridedamos siuntos
def addShipments(m, n, r_id):
    for i in range(m, n):
        with codecs.open('shipments/shipment'+str(i+1)+'.json', encoding="utf-8") as json_file:
            shipment = json.load(json_file)
            shipment["maršrutoID"] = routes.find()[r_id]["_id"]
            shipments.insert_one(shipment)

# ------------------- UŽKLAUSOS -------------------

# [1] Visų siuntų siuntėjų adresai
def findNames():
    for x in shipments.find():
        print(x["siuntėjas"]["adresas"])

# [2] Kiekvienam maršrutui (ar kurjeriui) priklausančių siuntų bendras svoris
def findShipmentWeight():
    ships = shipments.aggregate([
        { "$group":{ "_id":"$maršrutoID", "bendras_svoris":{"$sum":"$svoris"} } },
        { "$sort":{ "bendras_svoris":-1 } }
    ])
    for x in ships:
        print(x)

# [3] findShipmentWeight su map reduce
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

choice = int(input(
    "[1] 1 užklausa (visų siuntėjų adresai iš siuntų kolekcijos)\n" +
    "[2] 2 užklausa (kiekvienam maršrutui priklausančių siuntų bendras svoris)\n" + 
    "[3] 2 užklausa su map reduce\n"
))

match choice:
    case 1:
        findNames()
    case 2:
        findShipmentWeight()
    case 3:
        findShipmentWeightMapReduce()

client.close()