from .base_analyzer import BaseAnalyzer

class ProductPreferenceAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        return data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
