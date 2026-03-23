import pandas as pd

class DataCleaner:
    def clean(self, df):
        df.dropna(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Quantity'] = df['Quantity'].astype(int)
        df['Unit Price'] = df['Unit Price'].astype(float)
        df['Total'] = df['Total'].astype(float)
        return df
