import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('/Users/alexjones/Desktop/CSV_SQL/Football_match_prediction/data/csv/dataset.csv')

engine = create_engine('sqlite:///database.db')

df.to_sql('table_1', con=engine, if_exists='replace', index=False)

