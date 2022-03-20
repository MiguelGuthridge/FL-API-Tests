"""Test case manager

Keeps track of all test cases
"""

from typing import Callable, Optional
from fltest.testcase import TestCase, SimpleTest

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

def flTest():
    """Register a test case

    This function can be used as a decorator for test cases

    Args:
        test (type[TestCase]): test to register

    Returns:
        type[TestCase]: that same test
    """
    def decorator(test: type[TestCase]) -> type[TestCase]:
        MANAGER.register(test())
        return test
    return decorator

def flSimpleTest(
    min_version: int = -1,
    unsafe: bool = False
):
    """Register a simple test function

    This should be used to decorate a function that takes no arguments and
    returns None

    Args:
        test (Callable[[None], None]): test function

    Returns:
        Callable[[None], None]: test function
    """
    def decorator(test: Callable[[], None]):
        MANAGER.register(SimpleTest(test, min_version, unsafe))
        return test
    return decorator
