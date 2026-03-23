from .base_analyzer import BaseAnalyzer

class WeeklySalesAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        data['Week'] = data['Date'].dt.to_period('W').apply(lambda r: r.start_time)
        return data.groupby('Week')['Total'].sum()
