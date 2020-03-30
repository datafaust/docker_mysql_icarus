print('i am running every minute...')
from traffic.data import opensky
from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import sqlalchemy
import string
import io
import gc
import sys


#connection and host information
host = 'localhost'
db='icarus'
engine = create_engine('mysql+pymysql://root:password@'+ host+ ':3306/'+ db) #create engine connection
version= sys.version_info[0]

#functions to upload data
def upload(df,table_name):
    df.to_sql(table_name,con=engine,index=False,if_exists='append')
    engine.dispose()
    print('SUCCESSFULLY LOADED DATA INTO STAGING...')

#pull data drom api
sv = opensky.api_states()
final_df = sv.data
#quick column clean up 
#print(final_df.head())
final_df=final_df.rename(columns = {'timestamp':'time_stamp'})


#insert data to staging

try:
    upload(final_df, 'flights_stg')
except:
    print('ISSUE LOADING...')
del(final_df)
gc.collect()