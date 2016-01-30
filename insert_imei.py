from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_imei(query, args):

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            mensaje = ('Last insert id: %s' % (cursor.lastrowid,) )
            print(mensaje)
        else:
           mensaje = 'Last insert id not found'

        conn.commit()
        
    
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        
    return mensaje    