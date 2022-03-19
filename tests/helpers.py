"""
tests > helpers

Helper functions for tests
"""

def floatApproxEq(expected: float, actual: float) -> bool:
    """
    Return whether there is less than a 5% error between the expected
    and actual values, or if the expected value is zero, whether the actual
    value is within 0.001 of it.
    """
    if expected == 0:
        return abs(actual) < 0.001
    return abs(expected - actual) / abs(expected) < 0.05
