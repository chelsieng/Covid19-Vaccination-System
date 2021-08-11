import sshtunnel
import pymysql


#    SSH Hostname : login.encs.concordia.ca
#    SSH Username : your personal GCS/ENCS username
#    MYSQL Hostname : ujc353.encs.concordia.ca
#    MYSQL Server Port: 3306
#    Username: ujc353_1
#    Default Schema: ujc353_1

def getCursor():
    sshtunnel.SSH_TIMEOUT = 30000

    server = sshtunnel.SSHTunnelForwarder(
        'login.encs.concordia.ca',
        ssh_username="<your_personal_encs_username>",
        ssh_password="<your_personal_encs_password>",
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

    return db.cursor()


def get_Persons():
    cursor = getCursor()

    sql = "select * from Persons;"
    results = []
    try:
        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for item in results:
            print(item)
        # print(results)
    except:
        print("Error: unable to fetch data")
    # Table headers
    field_names = [i[0] for i in cursor.description]
    return field_names, results
