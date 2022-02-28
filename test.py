import pytest
import psycopg2
import config as cfg
import pandas as pd

# connect to the postgres server
conn = psycopg2.connect(database='airline', 
                        host='127.0.0.1', 
                        port='5432', 
                        user=cfg.user, 
                        password=cfg.password)

cur = conn.cursor()

def test_port_loc_dim():
    """
    Function: check that all rows were completely uploaded to port_loc_dim table
    """

    real_rows = pd.read_csv('data/port_loc.csv').shape[0]
    cur.execute('SELECT count(*) FROM port_loc_dim;')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_state_dim():
    """
    Function: check that all rows were completely uploaded to state_dim table
    """

    real_rows = pd.read_csv('data/states.csv').shape[0]
    cur.execute('SELECT count(*) FROM state_dim')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_airline_dim():
    """
    Function: check that all rows were completely uploaded to airline_dim table
    """

    real_rows = pd.read_csv('data/airline.csv').shape[0]
    cur.execute('SELECT count(*) FROM airline_dim')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_cancel_dim():
    """
    Function: check that all rows were completely uploaded to cancel_dim table
    """

    real_rows = pd.read_csv('data/cancellation.csv').shape[0]
    cur.execute('SELECT count(*) FROM cancel_dim')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_delay_dim():
    """
    Function: check that all rows were completely uploaded to delay_dim table
    """

    real_rows = pd.read_csv('data/delay_group.csv').shape[0]
    cur.execute('SELECT count(*) FROM delay_dim')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_distance_dim():
    """
    Function: check that all rows were completely uploaded to distance_dim table
    """

    real_rows = pd.read_csv('data/distance_group.csv').shape[0]
    cur.execute('SELECT count(*) FROM distance_dim')
    rows = cur.fetchone()[0]

    assert rows == real_rows

def test_airline_fact():
    """
    Function: check that all rows were completely uploaded to airline_fact table
    """

    real_rows = pd.read_csv('data/fact.csv').shape[0]
    cur.execute('SELECT count(*) FROM airline_fact')
    rows = cur.fetchone()[0]

    assert rows == real_rows