# drop tables
aircraft_dim_drop = 'DROP TABLE IF EXISTS aircraft_dim;'
airline_dim_drop = 'DROP TABLE IF EXISTS airline_dim;'
cancel_dim_drop = 'DROP TABLE IF EXISTS cancel_dim;'
delay_dim_drop = 'DROP TABLE IF EXISTS delay_dim;'
distance_dim_drop = 'DROP TABLE IF EXISTS distance_dim;'
port_loc_dim_drop = 'DROP TABLE IF EXISTS port_loc_dim;'
state_dim_drop = 'DROP TABLE IF EXISTS state_dim;'

airline_fact_drop = 'DROP TABLE IF EXISTS airline_fact;'

# create tables
aircraft_dim_create = """
CREATE TABLE IF NOT EXISTS aircraft_dim (
    c_aircraft varchar primary key,
    c_airline varchar
) 
"""

airline_dim_create = """
CREATE TABLE IF NOT EXISTS airline_dim (
    c_airline varchar primary key,
    airline_name varchar
)
"""

cancel_dim_create = """
CREATE TABLE IF NOT EXISTS cancel_dim (
    c_cancel varchar(1) primary key,
    cancel_des varchar 
)
"""

delay_dim_create = """
CREATE TABLE IF NOT EXISTS delay_dim (
    delay_group varchar primary key,
    time_range_minute varchar
)
"""

distance_dim_create = """
CREATE TABLE IF NOT EXIST distance_dim (
    distance_group varchar primary key,
    distance_range_mile varchar
)
"""

port_loc_dim_create = """
CREATE TABLE IF NOT EXISTS port_loc_dim (
    c_port varchar(5) primary key,
    city_name varchar,
    c_state varchar(2)
)
"""

state_dim_create = """
CREATE TABLE IF NOT EXISTS state_dim (
    c_state varchar(2) primary key,
    state_name varchar
)
"""

airline_fact_create = """
CREATE TABLE IF NOT EXISTS airline_fact (
    flight_date date,
    c_airline varchar,
    flight_num varchar,
    c_aircraft varchar,
    origin varchar,
    dest varchar,
    schedule_arr_time varchar,
    actual_arr_time varchar,
    arr_delay_group varchar,
    schedule_dep_time varchar,
    actual_dep_time varchar,
    dep_delay_group varchar,
    distance_group varchar,
    c_cancel varchar(1) 
)
"""

# insert into tables
aircraft_dim_insert = """
INSERT INTO aircraft_dim (
    c_aircrafe,
    c_airline
)
VALUES (%s, %s)
"""

airline_dim_insert = """
INSERT INTO airline_dim (
    c_airline,
    airline_name 
)
VALUES (%s, %s)
"""

cancel_dim_insert = """
INSERT INTO cancel_dim (
    c_cancel,
    cancel_des 
)
VALUES (%s, %s)
"""

delay_dim_insert = """
INSERT INTO delay_dim (
    delay_group,
    time_range_minute
)
VALUES (%s, %s)
"""

distance_dim_insert = """
INSERT INTO distance_dim (
    distance_group,
    distance_range_mile
)
VALUES (%s, %s)
"""

port_loc_dim_insert = """
INSERT INTO port_loc_dim (
    c_port,
    city_name,
    c_state
)
VALUES (%s, %s, %s)
"""

state_dim_insert = """
INSERT INTO state_dim (
    c_state,
    state_name
)
VALUES (%s, %s)
"""

airline_fact_insert = """
INSERT INTO airline_fact (
    flight_date,
    c_airline,
    flight_num,
    c_aircraft,
    origin,
    dest,
    schedule_arr_time,
    actual_arr_time,
    arr_delay_group,
    schedule_dep_time,
    actual_dep_time,
    dep_delay_group,
    distance_group,
    c_cancel 
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# query list
create_tables_query = [aircraft_dim_create, airline_dim_create, cancel_dim_create, delay_dim_create, distance_dim_create, port_loc_dim_create, state_dim_create]

drop_tables_query = [aircraft_dim_drop, airline_dim_drop, cancel_dim_drop, delay_dim_drop, distance_dim_drop, port_loc_dim_drop, state_dim_drop]