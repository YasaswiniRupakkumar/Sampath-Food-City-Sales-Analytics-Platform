# main.py
from reader import CSVReader
from cleaner import DataCleaner
from factory import AnalyzerFactory
from decorators.logger_decorator import AnalyzerLogger
from visualizer import SalesVisualizer

def main():
    file_path = "sales_data.csv"  # CSV file should exist with appropriate columns

    reader = CSVReader()
    raw_data = reader.read(file_path)

    cleaner = DataCleaner()
    data = cleaner.clean(raw_data)

    factory = AnalyzerFactory()

    options = ["branch", "product", "weekly", "preference", "distribution"]

    while True:
        print("\nSampath Food City (PVT) Ltd\n")
        print("1) Monthly sales analysis of each branch")
        print("2) Price analysis of each product")
        print("3) Weekly sales analysis of supermarket network")
        print("4) Product preference analysis")
        print("5) Analysis of the distribution of total sales amount of purchases")
        print("6) Exit")

        choice = int(input("Your Choice: "))

        if choice > 6 or choice < 1 :
            print("Invalid option! Try again.")
            continue
        if choice == 6:
            exit()
        
        analyzer = factory.create_analyzer(options[choice - 1])
        analyzer = AnalyzerLogger(analyzer)
        result = analyzer.analyze(data)
        print(f"\n===== {options[choice - 1].upper()} ANALYSIS RESULTS =====")
        print(result.head(10))  # Show top rows of results
        SalesVisualizer.plot(result, title=f"{options[choice - 1].capitalize()} Analysis")   
    

if __name__ == "__main__":
    main()
