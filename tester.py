
from typing import Callable

class TestCase:
    def __init__(self, test: Callable[[], None], location: str) -> None:
        self.test = test
        self.location = location

class TestManager:
    
    def __init__(self) -> None:
        self._tests: dict[str, list[TestCase]] = {}
    
    def __call__(self, test: Callable[[], None], location: str) -> Callable[[], None]:
        """Register a test with this test manager. This should be done using
        decorator syntax

        ```py
        @initTest
        def myTest():
            ...
        ```

        ## Args:
        * `test` (`Callable[[], None]`): test function to register
        * `location` (`str`): location of test (since access to the inspect
          module isn't allowed in FL Studio)

        ## Returns:
        * `Callable[[], None]`: test function
        """
        if location in self._tests:
            self._tests[location].append(TestCase(test, location))
        else:
            self._tests[location] = [TestCase(test, location)]
        return test
