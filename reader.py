import pandas as pd

class CSVReader:
    def read(self, filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"Failed to read file: {e}")
            return pd.DataFrame()
