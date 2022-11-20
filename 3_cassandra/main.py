from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])

session = cluster.connect('courier_service')

def createTables():
    session.execute("DROP TABLE IF EXISTS routes_by_municipality;")
    session.execute(
        '''
        CREATE TABLE routes_by_municipality(
            routeID INT,
            municipality TEXT,
            PRIMARY KEY((municipality), routeID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS shipments_by_route;")
    session.execute(
        '''
        CREATE TABLE shipments_by_route(
            shipmentID INT,
            senderID INT,
            receiverID INT,
            routeID INT,
            weight FLOAT,
            volume FLOAT,
            state TEXT,
            addressID INT,
            PRIMARY KEY((routeID), shipmentID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS shipments;")
    session.execute(
        '''
        CREATE TABLE shipments(
            shipmentID INT,
            senderID INT,
            receiverID INT,
            routeID INT,
            weight FLOAT,
            volume FLOAT,
            state TEXT,
            addressID INT,
            PRIMARY KEY(shipmentID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS person;")
    session.execute(
        '''
        CREATE TABLE person(
            personID INT,
            name TEXT,
            lastName TEXT,
            phoneNumber TEXT,
            adresoID INT,
            companyName TEXT,
            PRIMARY KEY(personID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS shipments_by_sender;")
    session.execute(
        '''
        CREATE TABLE shipments_by_sender(
            shipmentID INT,
            senderID INT,
            PRIMARY KEY((senderID), shipmentID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS shipments_by_receiver;")
    session.execute(
        '''
        CREATE TABLE shipments_by_receiver(
            shipmentID INT,
            receiverID INT,
            PRIMARY KEY((receiverID), shipmentID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS shipments_by_state;")
    session.execute(
        '''
        CREATE TABLE shipments_by_state(
            shipmentID INT,
            senderID INT,
            receiverID INT,
            routeID INT,
            weight FLOAT,
            volume FLOAT,
            state TEXT,
            addressID INT,
            PRIMARY KEY((state), shipmentID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS address;")
    session.execute(
        '''
        CREATE TABLE address(
            addressID INT,
            city TEXT,
            street TEXT,
            building TEXT,
            flat INT,
            routeID INT,
            PRIMARY KEY(addressID)
        );
        '''
    )
    session.execute("DROP TABLE IF EXISTS address_by_route;")
    session.execute(
        '''
        CREATE TABLE address_by_route(
            addressID INT,
            city TEXT,
            street TEXT,
            building TEXT,
            flat INT,
            routeID INT,
            PRIMARY KEY((routeID), addressID)
        );
        '''
    )

def insertRoutesByMunicip():
    session.execute("INSERT INTO routes_by_municipality (routeID, municipality) VALUES (33, 'Švenčionių r.') IF NOT EXISTS;")
    session.execute("INSERT INTO routes_by_municipality (routeID, municipality) VALUES (32, 'Vilniaus r.') IF NOT EXISTS;")
    session.execute("INSERT INTO routes_by_municipality (routeID, municipality) VALUES (31, 'Vilniaus m.') IF NOT EXISTS;")
    session.execute("INSERT INTO routes_by_municipality (routeID, municipality) VALUES (30, 'Vilniaus m.') IF NOT EXISTS;")
    session.execute("INSERT INTO routes_by_municipality (routeID, municipality) VALUES (29, 'Vilniaus m.') IF NOT EXISTS;")
def insertShipsByRoute():
    session.execute(
        '''
            INSERT INTO shipments_by_route (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (1, 1, 2, 29, 4.5, 0.001, 'Terminale', 1)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments_by_route (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (2, 1, 3, 33, 10, 0.01, 'Perduota kurjeriui', 3)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments_by_route (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (3, 4, 5, 33, 0.75, 0.0005, 'Perduota kurjeriui', 5)
            IF NOT EXISTS;
        '''
    )
def insertShips():
    session.execute(
        '''
            INSERT INTO shipments (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (1, 1, 2, 29, 4.5, 0.001, 'Terminale', 1)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (2, 1, 3, 33, 10, 0.01, 'Perduota kurjeriui', 3)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (3, 4, 5, 33, 0.75, 0.0005, 'Perduota kurjeriui', 5)
            IF NOT EXISTS;
        '''
    )
def insertPerson():
    session.execute(
        '''
            INSERT INTO person (personID, name, lastName, phoneNumber, adresoID, companyName)
            VALUES (1, null, null, '861122333', 1, 'Pigu.lt')
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO person (personID, name, lastName, phoneNumber, adresoID, companyName)
            VALUES (2, 'Antanas', 'Smetona', '861245780', 2, null)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO person (personID, name, lastName, phoneNumber, adresoID, companyName)
            VALUES (3, 'Kristijonas', 'Donelaitis', '867888997', 3, null)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO person (personID, name, lastName, phoneNumber, adresoID, companyName)
            VALUES (4, null, null, '867877891', 4, 'Senukai')
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO person (personID, name, lastName, phoneNumber, adresoID, companyName)
            VALUES (5, 'Vincas', 'Mykolaitis-Putinas', '863343433', 5, null)
            IF NOT EXISTS;
        '''
    )
def insertShipsBySender():
    session.execute("INSERT INTO shipments_by_sender (shipmentID, senderID) VALUES (1, 1) IF NOT EXISTS;")
    session.execute("INSERT INTO shipments_by_sender (shipmentID, senderID) VALUES (2, 1) IF NOT EXISTS;")
    session.execute("INSERT INTO shipments_by_sender (shipmentID, senderID) VALUES (3, 4) IF NOT EXISTS;")
def insertShipsByReceiver():
    session.execute("INSERT INTO shipments_by_receiver (shipmentID, receiverID) VALUES (1, 2) IF NOT EXISTS;")
    session.execute("INSERT INTO shipments_by_receiver (shipmentID, receiverID) VALUES (2, 3) IF NOT EXISTS;")
    session.execute("INSERT INTO shipments_by_receiver (shipmentID, receiverID) VALUES (3, 5) IF NOT EXISTS;")
def insertShipsByState():
    session.execute(
        '''
            INSERT INTO shipments_by_state (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (1, 1, 2, 29, 4.5, 0.001, 'Terminale', 1)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments_by_state (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (2, 1, 3, 33, 10, 0.01, 'Perduota kurjeriui', 3)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO shipments_by_state (shipmentID, senderID, receiverID, routeID, weight, volume, state, addressID)
            VALUES (3, 4, 5, 33, 0.75, 0.0005, 'Perduota kurjeriui', 5)
            IF NOT EXISTS;
        '''
    )
def insertAddress():
    session.execute(
        '''
            INSERT INTO address (addressID, city, street, building, flat, routeID)
            VALUES (1, 'Vilnius', 'Ukmergės', '1', null, 29)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address (addressID, city, street, building, flat, routeID)
            VALUES (2, 'Vilnius', 'Ateities', '1A', 2, 31)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address (addressID, city, street, building, flat, routeID)
            VALUES (3, 'Vilnius', 'Didlaukio', '1', 1, 31)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address (addressID, city, street, building, flat, routeID)
            VALUES (4, 'Vilnius', 'Ukmergės', '2', null, 29)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address (addressID, city, street, building, flat, routeID)
            VALUES (5, 'Švenčionys', 'Vilniaus', '1', null, 33)
            IF NOT EXISTS;
        '''
    )
def insertAddressByRoute():
    session.execute(
        '''
            INSERT INTO address_by_route (addressID, city, street, building, flat, routeID)
            VALUES (1, 'Vilnius', 'Ukmergės', '1', null, 29)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address_by_route (addressID, city, street, building, flat, routeID)
            VALUES (2, 'Vilnius', 'Ateities', '1A', 2, 31)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address_by_route (addressID, city, street, building, flat, routeID)
            VALUES (3, 'Vilnius', 'Didlaukio', '1', 1, 31)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address_by_route (addressID, city, street, building, flat, routeID)
            VALUES (4, 'Vilnius', 'Ukmergės', '2', null, 29)
            IF NOT EXISTS;
        '''
    )
    session.execute(
        '''
            INSERT INTO address_by_route (addressID, city, street, building, flat, routeID)
            VALUES (5, 'Švenčionys', 'Vilniaus', '1', null, 33)
            IF NOT EXISTS;
        '''
    )
# createTables()
# insertRoutesByMunicip()
# insertShipsByRoute()
# insertShips()
# insertPerson()
# insertShipsBySender()
# insertShipsByReceiver()
# insertShipsByState()
# insertAddress()
# insertAddressByRoute()

# -------------------- UŽKLAUSOS -----------------------

# Rodyti maršrutus pagal savivaldybę (municiaplity = Švenčionių r.)
def Q1():
    output = session.execute("SELECT * FROM routes_by_municipality WHERE municipality = 'Švenčionių r.';")
    return output

# Rodyti siuntas pagal maršruto numerį (routeID = 33)
def Q2():
    output = session.execute("SELECT * FROM shipments_by_route WHERE routeID = 33;")
    return output

# Rodyti siuntos informaciją
def Q3():
    output = session.execute("SELECT * FROM shipments")
    return output

# Rodyti siuntėjo/gavėjo informaciją
def Q4():
    output = session.execute("SELECT * FROM person")
    return output

# Rodyti asmens išsiųstas siuntas (senderID = 1)
def Q5():
    output = session.execute("SELECT * FROM shipments_by_sender WHERE senderID = 1")
    return output

# Rodyti asmens gautas siuntas (receiverID = 2)
def Q6():
    output = session.execute("SELECT * FROM shipments_by_receiver WHERE receiverID = 2")
    return output

# Rodyti siuntas pagal būseną (state = Perduota kurjeriui)
def Q7():
    output = session.execute("SELECT * FROM shipments_by_state WHERE state = 'Perduota kurjeriui'")
    return output

# Rodyti pristatymo adresą (addressID = 5)
def Q8():
    output = session.execute("SELECT * FROM address WHERE addressID = 5")
    return output

# Rodyti adresus pagal maršrutoID (routeID = 33)
def Q9():
    output = session.execute("SELECT * FROM address_by_route WHERE routeID = 29")
    return output

result = Q1()
for row in result:
    print(row)