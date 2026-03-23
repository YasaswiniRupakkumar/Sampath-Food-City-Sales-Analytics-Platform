import matplotlib.pyplot as plt
import pandas as pd

class SalesVisualizer:
    @staticmethod
    def plot(data, title="Analysis"):
        if isinstance(data, pd.Series) and data.name == "Total":
            data.plot(kind='hist', bins=10, title=title)
        elif isinstance(data, pd.Series):
            data.plot(kind='bar', title=title)
        elif isinstance(data, pd.DataFrame):
            data.plot(kind='bar', stacked=True, title=title)
        else:
            print(f"Plot not supported for this data: {data}")
            return
        plt.tight_layout()
        plt.show()
