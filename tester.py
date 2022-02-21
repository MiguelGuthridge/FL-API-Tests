
from typing import Callable, Optional
import config

TestFunction = Callable[[], None]

class TestResult:
    def __init__(
        self,
        test: TestFunction,
        location: str,
        succeeded: bool,
        exception: Optional[Exception],
    ) -> None:
        self.test = test
        self.location = location
        self.succeeded = succeeded
        self.exception = exception
    
    def __bool__(self) -> bool:
        return self.succeeded

class TestCase:
    def __init__(self, test: TestFunction, location: str) -> None:
        self.test = test
        self.location = location
    
    def run(self) -> TestResult:
        try:
            self.test()
        except Exception as e:
            return TestResult(
                self.test,
                self.location,
                False,
                e
            )
        return TestResult(
            self.test,
            self.location,
            True,
            None
        )

class TestManager:
    """Manages registering and running tests
    """
    def __init__(self) -> None:
        self._tests: dict[str, list[TestCase]] = {}
    
    def __call__(self, test: TestFunction, location: str) -> TestFunction:
        """Register a test with this test manager. This should be done using
        decorator syntax

        ```py
        # Create a test for a function in the general module
        @initTest("general")
        def myTest():
            ...
        ```

        ## Args:
        * `test` (`Callable[[], None]`): test function to register
        * `location` (`str`): module that we're testing (since access to the
          inspect module isn't allowed in FL Studio)

        ## Returns:
        * `Callable[[], None]`: test function
        """
        if location in self._tests:
            self._tests[location].append(TestCase(test, location))
        else:
            self._tests[location] = [TestCase(test, location)]
        return test
    
    def run(self):
        # Run each test in each category
        for location in self._tests:
            print(f"Testing <{location}>... ")
            passed = 0
            failures: list[TestResult] = []
            total = 0
            for t in self._tests[location]:
                if config.PRINT_EACH_TEST:
                    print(f" -> {t.test} : ", end='')
                if result := t.run():
                    if config.PRINT_EACH_TEST:
                        print(f"Passed")
                    passed += 1
                else:
                    failures.append(result)
                    if config.PRINT_EACH_TEST:
                        print(f"Failed")
                total += 1
            print(f"{passed}/{total} passed")
            for f in failures:
                print(f" -> {f.test}:")
                if f.exception is not None:
                    print(f.exception.__traceback__)
                else:
                    print("No traceback provided")
            print()
        
initTest = TestManager()
idleTest = TestManager()
midiTest = TestManager()
