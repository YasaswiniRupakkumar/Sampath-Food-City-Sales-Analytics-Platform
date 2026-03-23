from .base_analyzer import BaseAnalyzer

class SalesDistributionAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        return data['Total']
