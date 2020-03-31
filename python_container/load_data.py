print('i am running every minute...')
from traffic.data import opensky
from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import sqlalchemy
import gc
import sys

#connection and host information
host = 'mysql'
db='icarus'
engine = create_engine('mysql+pymysql://root:password@'+ host+ ':3306/'+ db) #create engine connection
version= sys.version_info[0]

#function loads data
def upload(df,table_name):
    df.to_sql(table_name,con=engine,index=False,if_exists='append')
    #engine.dispose()
    print('SUCCESSFULLY LOADED DATA INTO STAGING...')

#function calls api
def callData():
    sv = opensky.api_states()
    final_df = sv.data
    final_df=final_df.rename(columns = {'timestamp':'time_stamp'})
    return final_df

#call api
try:
    final_df = callData()
except Exception as error:
        print('Caught this error: ' + repr(error))

#insert data to staging
try:
    upload(final_df, 'flights_stg')
except Exception as error:
        print('Caught this error: ' + repr(error))

#print(final_df.head())
del(final_df)
gc.collect()

#execute production insert
with engine.connect().execution_options(autocommit=True) as con:
    try:
        con.execute('CALL icarus.insertPrdData();')
        print('SUCCESSFULLY INSERTED DATA INTO PRODUCTION...')
    except Exception as error:
        print('Caught this error: ' + repr(error))
    
    try:
        con.execute('CALL icarus.deleteStgData();')
        print('SUCCESSFULLY DELETED STAGE DATA...')
    except Exception as error:
        print('Caught this error: ' + repr(error))
    con.close()
    engine.dispose()

    


