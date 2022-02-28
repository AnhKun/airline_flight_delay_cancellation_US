# Flight cancellation and delay during Covid-19 in US
The purpose of this project is to give the first hands-on experience about modeling and uploading datasets into Postgres server or into data storage such as postgres database or data warehouse for further analysis.
### 1. Dataset
This dataset is taken from Kaggle. 
<br>For more infomation about the dataset, it's [here](https://www.kaggle.com/akulbahl/covid19-airline-flight-delays-and-cancellations)
<br>For the technique I used to download the dataset, it's *opendatasets*.
```
import opendatasets as od
od.download(<url-of-the-dataset-on-kaggle>)
```
### 2. Environment
In this project, I used docker to run the virtual environment to use pyspark and Postgres server.
### 3. Instruction of the project
This project includes 5 files (.py and .ipynb). They are:
- **wrangling.ipynb**: clean the dataset and break it into smaller sub datasets.
- **sql_queries.py**: contain the queries to create, drop and insert values into the table.
- **modify_tables.py**: connect to the Postgres server; drop and create the database and necessary tables into Postgres.
- **elt.py**: connect to the Postgres server; insert values from sub datasets into tables in Postgres.
- **test.py**: use pytest to ensure that all records were completely uploaded.
- **analysis.ipynb**: make some analysis.

To manipulate and upload datasets to the Postgres server, we need to run the following order of the workflow: wrangling.ipynb >> sql_queries.py >> modify_tables.py >> etl.py >> test.py >> analysis.ipynb
### 4. Postgres Database
![](/data/entity_relationship.png)

- **airline_dim** contains airline carrier codes and names.

**airline_dim**|                       
---------------|
c_airline (PK) |
airline_name   |

- **cancel_dim** contains cancel codes (A: Carrier, B: Weather, C: National Aviation System, D: Security, O: Non-cancellation).

**cancel_dim**|
--------------|
c_cancel (PK) |
cancel_des    |

- **delay_dim** contains a range of numbers which is represented for 15-minute increments Rounded Down.

**delay_dim**     |
------------------|
delay_group (PK)  |
time_range_minute |

- **distance_dim** contains a range of numbers which is represented for 250-Mile increments Rounded Down.

**distance_dim**   |
-------------------|
distance_group (PK)|
distance_range_mile|

- **port_loc_dim** contains all airports in US.

**port_loc_dim**|
----------------|
c_port (PK)     |
city_name       |
c_state         |

- **state_dim** contains all states in US.

**state_dim**|
-------------|
c_state (PK) |
state_name   |

- **airline_fact** is the fact table in this dataset.

**airline_fact** |
-----------------|
flight_id (PK)   |
flight_date      |
c_airline        |
flight_num       |
c_aircraft       |
origin           |
dest             |
schedule_dep_time|
actual_dep_time  |
dep_delay_group  |
schedule_arr_time|
actual_arr_time  |
arr_delay_group  |
distance_group   |
c_cancel         |

**Note**: (PK) is the primary key.