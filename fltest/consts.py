
from typing import NewType

TestResult = NewType("TestResult", str)

FAILED  = TestResult('*')
PASSED  = TestResult('.')
SKIPPED = TestResult('?')
