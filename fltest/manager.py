"""Test case manager

Keeps track of all test cases
"""

from fltest.testcase import TestCase

class TestManager:
    """Manages test cases
    """

    def __init__(self) -> None:
        self._cases: list[TestCase] = []

    def register(self, case: TestCase) -> None:
        self._cases.append(case)

    def __iter__(self):
        return iter(self._cases)

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