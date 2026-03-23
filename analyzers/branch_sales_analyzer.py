from .base_analyzer import BaseAnalyzer

class BranchSalesAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        result = data.groupby([data['Date'].dt.to_period('M'), 'Branch'])['Total'].sum()
        return result.unstack().fillna(0)
