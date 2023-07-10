import datetime
import os

from colorama import Fore, Style

def pytest_terminal_summary(terminalreporter):
    # Generate a unique filename using timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"test_results/test_results_{timestamp}.txt"

    # Construct the full file path
    filepath = os.path.join(os.getcwd(), filename)

    # Write the test results to the file
    with open(filepath, "w") as f:
        for report in terminalreporter.stats.get("passed", []) + terminalreporter.stats.get("failed", []):
            f.write(f"Test: {Style.BRIGHT}{Fore.BLUE}{report.nodeid}{Style.RESET_ALL}\n")
            outcome = "PASSED" if report.passed else "FAILED"
            outcome_color = Fore.GREEN if report.passed else Fore.RED

            f.write(f"Outcome: {outcome_color}{outcome}{Style.RESET_ALL}\n")

            if not report.passed:
                f.write("Stack Trace:\n")
                f.write(report.longreprtext + "\n")
            f.write(f"Location: {report.location}\n")
            f.write("---------------------------\n")
