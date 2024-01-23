import pandas as pd
from sqlalchemy import create_engine

url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'

def add_data(url):
    #data to be added
    df = pd.read_csv(url,nrows=100)

    #change column types
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    #connect to postgres
    
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    engine.connect()
    
    #create ddl
    df.head(n=0).to_sql('ny_taxi', con=engine, if_exists = 'replace')
    print(pd.read_sql(query, con=engine))

    #load rest of the data
    df_iterator = pd.read_csv(url, iterator = True, chunksize= 100000)
    
    while True: 

        try:
            
            df = next(df_iterator)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name='ny_taxi', con=engine, if_exists='append')


        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break
    
    
    
add_data(url)