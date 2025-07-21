import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class FetchMedicalInno:
    def __init__(self):
        load_dotenv()
        self.engine = self._create_engine()

    def _create_engine(self):
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        port = os.getenv("MYSQL_PORT", 3306)
        database = os.getenv("MYSQL_DATABASE")
        return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", echo=True)

    def fetch_table(self, table_name, output_file):
        query = f"SELECT * FROM {table_name} LIMIT 1000"
        df = pd.read_sql(query, con=self.engine)
        df.to_csv(output_file, index=False, encoding='utf-8-sig')

    def fetch_all(self):
        self.fetch_table("consultation", "consultation.csv")
        self.fetch_table("speciality", "specialty.csv")
        self.fetch_table("consultation_speciality", "consultation_specialty.csv")
        self.fetch_table("service_question", "service_question.csv")

    def merge_tables(self):
        specialty = pd.read_csv("specialty.csv")
        consultation = pd.read_csv("consultation.csv")
        consultation_specialty = pd.read_csv("consultation_specialty.csv")
        service_question = pd.read_csv("service_question.csv")

        merged1 = pd.merge(consultation, consultation_specialty, on='consultation_id', how='inner')
        merged2 = pd.merge(merged1, specialty, on='specialty_id', how='inner')
        merged_final = pd.merge(merged2, service_question, on='service_question_id', how='inner')

        merged_final.to_csv('merged_final.csv', index=False, encoding='utf-8-sig')
