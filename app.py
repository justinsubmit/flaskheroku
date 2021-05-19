from flask import Flask
from mysql.connector import pooling
from config.Settings import Settings

import os
app = Flask(__name__)


# http://localhost:5000?data=test@test.com
@app.route('/')
def validate():
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'
    host=os.environ['HOST2']
    database=os.environ['DATABASE2']
    user=os.environ['USERNAME2']
    password=os.environ['PASSWORD2']
    print("host2",host)
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host=host,
                                                  database=database,
                                                  user=user,
                                                  password=password)
    dbConn = connection_pool.get_connection()
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'

    #Production
    # host=os.environ['HOST2']
    # database=os.environ['DATABASE2']
    # user=os.environ['USERNAME2']
    # password=os.environ['PASSWORD2']
    # dbConn.close()
    return "hello"


@app.route('/users')
def validate2():
    host='localhost'
    database='furniture'
    user='root'
    password='Singapore1'
    host=os.environ['HOST2']
    database=os.environ['DATABASE2']
    user=os.environ['USERNAME2']
    password=os.environ['PASSWORD2']
    print("host2",host)
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host=host,
                                                  database=database,
                                                  user=user,
                                                  password=password)
    dbConn = connection_pool.get_connection()
    cursor = dbConn.cursor(dictionary=True)
    sql="select * from user"
    cursor.execute(sql)
    users = cursor.fetchall()

    # dbConn.close()
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'

    #Production
    # host=os.environ['HOST2']
    # database=os.environ['DATABASE2']
    # user=os.environ['USERNAME2']
    # password=os.environ['PASSWORD2']
   
    return "users"    




if __name__ == '__main__':
    app.run(debug=True)
