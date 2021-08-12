import sshtunnel
import pymysql
import json
from django.core.serializers.json import DjangoJSONEncoder
import os

# from dotenv import load_dotenv

# load_dotenv()

encsUser = os.getenv('ENCS_USERNAME')
encsPass = os.getenv('ENCS_PASSWORD')


#    SSH Hostname : login.encs.concordia.ca
#    SSH Username : your personal GCS/ENCS username
#    MYSQL Hostname : ujc353.encs.concordia.ca
#    MYSQL Server Port: 3306
#    Username: ujc353_1
#    Default Schema: ujc353_1

def getDBCursor():
    sshtunnel.SSH_TIMEOUT = 30000

    server = sshtunnel.SSHTunnelForwarder(
        'login.encs.concordia.ca',
        ssh_username=encsUser,
        ssh_password=encsPass,
        remote_bind_address=('ujc353.encs.concordia.ca', 3306)
    )

    server.start()
    print(server.local_bind_port)

    print("Connected to server")

    db = pymysql.connect(
        host="localhost",
        port=server.local_bind_port,
        user="ujc353_1",
        password="1qaz2wsx",
        database="ujc353_1",
        connect_timeout=3100)

    return db, db.cursor()


def getQuery(query):
    db, cursor = getDBCursor()
    sql = query
    data = {"attributes": [], "results": []}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        db.commit()

        # Fetch all the rows in a list of lists.
        data["results"] = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # Table headers
    data["attributes"] = [i[0] for i in cursor.description]
    db.close()
    return json.dumps(data, cls=DjangoJSONEncoder)


def delete(query):
    db, cursor = getDBCursor()
    sql = query
    print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        db.commit()
        return True

    except:
        print("Error: unable to delete")
        return False


def edit(query):
    db, cursor = getDBCursor()
    sql = query
    try:
        # Execute the SQL command
        cursor.execute(sql)
        db.commit()
        return True

    except:
        print("Error: unable to edit")
        return False


def create(query):
    db, cursor = getDBCursor()
    sql = query
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        print('Error: unable to create')
        return False
