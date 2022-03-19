"""
tests > framework > framework

Tests for the testing framework
"""
from fltest import TestCase, flTest, flSimpleTest

# Example test case
@flTest()
class ExampleTest(TestCase):
    def __init__(self) -> None:
        super().__init__(details="A basic test to ensure the testing "
                         "framework is working correctly")

    def activate(self) -> None:
        self.markSuccess()

@flSimpleTest(min_version=20)
def exampleTest():
    assert 1 == 1
