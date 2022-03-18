
from testcase import TestCase


class TestManager:
    """Manages test cases
    """

    def __init__(self) -> None:
        self._cases: list[TestCase] = []

    def register(self, case: TestCase) -> None:
        self._cases.append(case)

    def __iter__(self):
        return iter(self._cases)
