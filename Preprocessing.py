import pandas as pd
class Preprocessing:
    def __init__(self , df , df2):
        self.df = df
        self.df2 = df2
    def read_data(self , df , df2):
        self.df = pd.read_csv(r"C:\Users\khala\Downloads\specialty.csv")
        self.df2 = df

    def fill_null_values(self , df , df2 ):
        df2 = df['slug_ar'].fillna('Unknown')
        df2 = df['slug_en'].fillna('Unknown')
        df2 = df['type'].fillna(0)
        df2 = df['user_id'].fillna('Unknown')
        df2 = df['last_modified_by_user_id'].fillna('System')

    def remove_duplicates(self , df , df2):
        df2 = df.drop_duplicates()




