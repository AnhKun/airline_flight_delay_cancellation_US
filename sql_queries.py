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
