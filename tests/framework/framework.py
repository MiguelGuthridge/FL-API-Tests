"""
tests > framework > framework

Tests for the testing framework
"""

import playlist

from fltest import TestCase, flTest, flSimpleTest

# Example test case
@flTest()
class ClassTest(TestCase):
    """A simple test class to ensure the framework is working correctly
    """
    def activate(self) -> None:
        self.markSuccess()

@flSimpleTest()
def functionTest():
    """A simple test function to ensure the framework is working correctly
    """
    assert 1 == 1

@flSimpleTest()
def checkFile():
    """Ensure the 'API Test Project.flp' project is loaded"""
    assert playlist.getTrackName(1) == "Example Track"
