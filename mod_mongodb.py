# Pour mongodb, il faut lancer le docker-compose.
# Mon mongo est dans un container
import csv
import json

from pymongo import MongoClient
from pymongo.errors import OperationFailure

mongoServerUrl = 'mongodb://localhost' # if tested outside container. mongodb://mongo from Docker
mongoServerPort = 27017


def getStadesCollection():
    # if mypyapp tested directly outside python container
    clientConnection = MongoClient(mongoServerUrl, mongoServerPort)

    try:
        # Try to validate a collection, if it fails, create collection (see except)
        clientConnection.db.validate_collection("MG_STADES")
        stadesCollection = clientConnection.db.MG_STADES
        # =================empty collection to avoid multiple savings=================
        stadesCollection.delete_many({})
    except OperationFailure:
        #print("This collection doesn't exist. create it")
        stadesCollection = clientConnection.db.MG_STADES

    return stadesCollection


def saveItem(coll, item):
    saved_id = coll.insert_one(item).inserted_id
    if not saved_id:
        print('Attention, stade non enregistré. A Débugguer!')


def listItems(coll, keyToFilter = None, valueToFiler = None):
    if not keyToFilter or not ValueError:
        results = coll.find()
    else:
        results = coll.find({keyToFilter : valueToFiler})

    for i in results:
        print(i)


if __name__ == "__main__":
    stadesCollection = getStadesCollection()

    with open('stadiums_sortie.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None)
        for row in csv_reader:
            token = row[0].split(';')
            item_stade = {}
            item_stade['team'] = token[0]
            item_stade['city'] = token[1].strip('\"')
            item_stade['stadium'] = token[2].strip('\"')
            item_stade['capacity'] = int(token[3].strip('\"'))
            item_stade['country'] = token[4].strip('\"')
            #print(item_stade)
            saveItem(stadesCollection, item_stade)

    listItems(stadesCollection)

    listItems(stadesCollection, 'country', 'England')