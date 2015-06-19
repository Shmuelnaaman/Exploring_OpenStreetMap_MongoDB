

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]

    return db


def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche
    query = {"manufacturer": "Porsche"}
    return query


def find_porsche(db, query):
    return db.autos.find(query)


if __name__ == "__main__":

    db = get_db('jeru')
    query = porsche_query()
    p = find_porsche(db, query)
    print db.cities.find_one()
