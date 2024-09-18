import os
import pandas as pd
import configparser
from pgdb import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname,'config.ini'))

DATABASE_CREDS = config['Database']

files = os.listdir(dirname)
file_list = []
for file in files:
    if os.path.splitext(os.path.join(dirname, file))[1] == '.csv':
        file_list.append(file)

report_df = pd.concat(map(pd.read_csv, file_list), ignore_index=True) 

for file in file_list:
    os.remove(os.path.join(dirname, file))

database = PGDatabase(
    host=DATABASE_CREDS['HOST'],
    database=DATABASE_CREDS['DATABASE'],
    user=DATABASE_CREDS['USER'],
    password=DATABASE_CREDS['PASSWORD']
    )

for i, row in report_df.iterrows():
    query = f"""insert into reports values (
    '{row['shop_number']}', 
    '{row['cash_number']}', 
    '{row['doc_id']}',
    '{row['item']}', 
    '{row['category']}', 
    {row['amount']},
    {row['price']},
    {row['discount']})"""
    database.post(query)