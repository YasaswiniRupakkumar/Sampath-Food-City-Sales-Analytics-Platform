class AnalyzerLogger:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self, data):
        print(f"[LOG] Starting {self.analyzer.__class__.__name__}")
        result = self.analyzer.analyze(data)
        print(f"[LOG] Completed {self.analyzer.__class__.__name__}")
        return result
