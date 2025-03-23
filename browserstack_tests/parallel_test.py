import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from test_script import run_browserstack_test

def run_tests_in_parallel():
    """Runs BrowserStack tests in parallel on multiple browsers and devices"""

    test_cases = [
        ("chrome", "Windows", "10"),
        ("firefox", "Windows", "10"),
        ("safari", "OS X", "Monterey"),
        (None, None, None, "iPhone 13", True),
        (None, None, None, "Samsung Galaxy S22", True),
    ]

    with ThreadPoolExecutor(max_workers=len(test_cases)) as executor:
        futures = {executor.submit(run_browserstack_test, *args): args for args in test_cases}

        for future in as_completed(futures):
            try:
                future.result()  # Runs each test case
            except Exception as e:
                print(f"Test failed for {futures[future]}: {e}")

if __name__ == "__main__":
    run_tests_in_parallel()
