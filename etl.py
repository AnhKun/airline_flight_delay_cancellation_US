import pandas as pd
from sql_queries import *
import psycopg2
import config

def process_data(cur, conn):
    # create the dataframe for each dataset
    airline_df = pd.read_csv('data/airline.csv')
    cancel_df = pd.read_csv('data/cancellation.csv')
    delay_df = pd.read_csv('data/delay_group.csv')
    distance_df = pd.read_csv('data/distance_group.csv')
    port_loc_df = pd.read_csv('data/port_loc.csv')
    state_df = pd.read_csv('data/states.csv')

    fact_df = pd.read_csv('data/fact.csv')

    # save value into postgress sever
    for _, row in airline_df.iterrows():
        cur.execute(airline_dim_insert, row)
        conn.commit()

    for _, row in cancel_df.iterrows():
        cur.execute(cancel_dim_insert, row)
        conn.commit()

    for _, row in delay_df.iterrows():
        cur.execute(delay_dim_insert, row)
        conn.commit()

    for _, row in distance_df.iterrows():
        cur.execute(distance_dim_insert, row)
        conn.commit()

    for _, row in port_loc_df.iterrows():
        cur.execute(port_loc_dim_insert, row)
        conn.commit()

    for _, row in state_df.iterrows():
        cur.execute(state_dim_insert, row)
        conn.commit()

    for _, row in fact_df.iterrows():
        cur.execute(airline_fact_insert, row)
        conn.commit()


def main():
    """
    """

    # connect to airline database
    conn = psycopg2.connect(database='airline', host='127.0.0.1', port='5432', user=config.user, password=config.password)
    cur = conn.cursor()

    process_data(cur, conn)

    conn.close()

if __name__ == '__main__':
    main()