from analyzers.branch_sales_analyzer import BranchSalesAnalyzer
from analyzers.product_price_analyzer import ProductPriceAnalyzer
from analyzers.weekly_sales_analyzer import WeeklySalesAnalyzer
from analyzers.product_preference_analyzer import ProductPreferenceAnalyzer
from analyzers.sales_distribution_analyzer import SalesDistributionAnalyzer

class AnalyzerFactory:
    def create_analyzer(self, analyzer_type):
        analyzers = {
            "branch": BranchSalesAnalyzer,
            "product": ProductPriceAnalyzer,
            "weekly": WeeklySalesAnalyzer,
            "preference": ProductPreferenceAnalyzer,
            "distribution": SalesDistributionAnalyzer,
        }
        analyzer_class = analyzers.get(analyzer_type)
        if analyzer_class:
            return analyzer_class()
        raise ValueError("Invalid analyzer type")
