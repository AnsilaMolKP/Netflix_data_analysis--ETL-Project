import kaggle
!kaggle datasets download shivamb/netflix-shows

import zipfile
with zipfile.ZipFile("netflix-shows.zip", "r") as zip_ref:
    zip_ref.extractall()
  
import pandas as pd 
df = pd.read_csv('netflix_titles.csv')
import sqlalchemy as sal
engine = sal.create_engine('mssql://localhost\\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()

df.to_sql('netflix_raw', con=conn , index=False, if_exists = 'append')
conn.close()

len(df)
df.head()
df[df.show_id=='s5023']
max(df.description.dropna().str.len())
df.isna().sum()
