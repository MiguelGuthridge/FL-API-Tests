"""Test case manager

Keeps track of all test cases
"""

from typing import Optional
from fltest.testcase import TestCase, TestSuccess

class TestManager:
    """Manages test cases
    """

    def __init__(self) -> None:
        self._cases: list[TestCase] = []

    def register(self, case: TestCase) -> None:
        self._cases.append(case)

    def __iter__(self):
        return iter(self._cases)

    def __len__(self) -> int:
        return len(self._cases)

MANAGER = TestManager()

def registerTest(test: type[TestCase]) -> type[TestCase]:
    """Register a test case

    This function can be used as a decorator for test cases

    Args:
        test (type[TestCase]): test to register

    Returns:
        type[TestCase]: that same test
    """
    MANAGER.register(test())
    return test

# Example test case
@registerTest
class ExampleTest(TestCase):
    def __init__(self, name: Optional[str] = None, details: str = "") -> None:
        super().__init__(name, details="A simple test to ensure the testing "
                         "framework is working correctly")
    def activate(self) -> None:
        assert 1 == 1
        raise TestSuccess
