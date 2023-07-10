import os
import unittest
import datetime


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.run_count = 0
        self.runs_per_file = 10
        self.current_file_path = self.get_file_path()
        self.file_path = self.get_file_path()

    def get_file_path(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        run_count = self.get_current_run_count()
        return f"test_results_{timestamp}_{run_count}.txt"

    def get_current_run_count(self):
        file_path = "current_run_count.txt"
        if not os.path.exists(file_path):
            return 1
        else:
            with open(file_path, "r") as f:
                return int(f.read())

    def update_run_count(self, current_run_count):
        file_path = "current_run_count.txt"
        with open(file_path, "w") as f:
            f.write(str(current_run_count))

    def startTestRun(self):
        self.stream.writeln(f"Test Run: {datetime.datetime.now()}")
        self.run_count += 1

        current_run_count = self.get_current_run_count()

        if current_run_count > self.runs_per_file:
            self.run_count = 1
            current_run_count = 1
            self.current_file_path = self.get_file_path()

        self.update_run_count(current_run_count + 1)

    def startTest(self, test):
        self.stream.writeln(f"Test {self.run_count} - {test.id()}")

    def addSuccess(self, test):
        self.stream.writeln("PASS")

    def addFailure(self, test, err):
        self.stream.writeln(f"FAIL: {err}")