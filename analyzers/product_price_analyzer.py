from .base_analyzer import BaseAnalyzer

class ProductPriceAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        return data.groupby('Product')['Unit Price'].agg(['mean', 'min', 'max', 'std'])
