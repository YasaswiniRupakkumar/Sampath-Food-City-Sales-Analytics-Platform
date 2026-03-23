import pandas as pd
from reader import CSVReader
from cleaner import DataCleaner
from analyzers.branch_sales_analyzer import BranchSalesAnalyzer
from analyzers.product_price_analyzer import ProductPriceAnalyzer
from analyzers.weekly_sales_analyzer import WeeklySalesAnalyzer
from analyzers.product_preference_analyzer import ProductPreferenceAnalyzer
from analyzers.sales_distribution_analyzer import SalesDistributionAnalyzer

reader = CSVReader()
cleaner = DataCleaner()
df = cleaner.clean(reader.read("sales_data.csv"))

def test_branch_sales_analyzer():
    analyzer = BranchSalesAnalyzer()
    result = analyzer.analyze(df)
    assert isinstance(result, pd.DataFrame)
    print("test_branch_sales_analyzer PASSED")

def test_product_price_analyzer():
    analyzer = ProductPriceAnalyzer()
    result = analyzer.analyze(df)
    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in ["mean", "min", "max", "std"])
    print("test_product_price_analyzer PASSED")

def test_weekly_sales_analyzer():
    analyzer = WeeklySalesAnalyzer()
    result = analyzer.analyze(df)
    assert isinstance(result, pd.Series)
    assert result.index.name == "Week"
    print("test_weekly_sales_analyzer PASSED")

def test_product_preference_analyzer():
    analyzer = ProductPreferenceAnalyzer()
    result = analyzer.analyze(df)
    assert isinstance(result, pd.Series)
    assert result.index.name == "Product"
    print("test_product_preference_analyzer PASSED")

def test_sales_distribution_analyzer():
    analyzer = SalesDistributionAnalyzer()
    result = analyzer.analyze(df)
    assert isinstance(result, pd.Series)
    assert result.name == "Total"
    print("test_sales_distribution_analyzer PASSED")

# Run tests manually (for IDLE or standard Python execution)
if __name__ == "__main__":
    test_branch_sales_analyzer()
    test_product_price_analyzer()
    test_weekly_sales_analyzer()
    test_product_preference_analyzer()
    test_sales_distribution_analyzer()
