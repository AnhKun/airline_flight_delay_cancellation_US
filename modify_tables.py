import psycopg2
from sql_queries import create_tables_query, drop_tables_query 
import config

def create_database():
    """
    Create and connect to airline database in postgreSQL
    """

    # connect to postgres database
    conn = psycopg2.connect(database='postgres', host='127.0.0.1', port='5432', user=config.user, password=config.password)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create airline database
    cur.execute("DROP DATABASE IF EXISTS airline;")
    cur.execute("CREATE DATABASE airline WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to postgres database
    conn.close()

    # connect to airline database
    conn = psycopg2.connect(database='airline', host='127.0.0.1', port='5432', user=config.user, password=config.password)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    return cur, conn

def drop_table(cur, conn):
    """
    Drops each table using the queries in `drop_tables_query` list.
    """

    for query in drop_tables_query:
        cur.execute(query)
        conn.commit()

def create_table(cur, conn):
    """
    Create each table using the queries in `create_tables_query` list
    """
    
    for query in create_tables_query:
        cur.execute(query)
        conn.commit()

def main():
    """
    Drop (if exist) airline database
    Create airline database
    Drop all tables 
    Create all tables
    Close connection
    """

    cur, conn = create_database()

    drop_table(cur, conn)
    create_table(cur, conn)

    conn.close()

if __name__ == '__main__':
    main()