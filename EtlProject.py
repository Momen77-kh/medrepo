import pandas as pd
from sqlalchemy import create_engine , text
from sqlalchemy.orm import Session

engine = create_engine('mysql+pymysql://reporting:Ka8c9*eA:63-GuF%7X@reporting2.cwlsvxzlhirz.eu-west-1.rds.amazonaws.com/medical_inno', echo=True)

df = pd.read_sql("select * from table_name", con=engine)

df.to_csv('results.csv', index=False, encoding='utf-8-sig')
