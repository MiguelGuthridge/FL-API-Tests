
import sys
import general
from typing import Optional, TypeVar, Callable
from typing_extensions import Self, ParamSpec, Concatenate

import config
from .consts import TestResult, PASSED, FAILED, SKIPPED
from fltest.testcase import TestCase, TestSuccess
from fltest.manager import MANAGER

P = ParamSpec("P")

def callWrapper(
    func: Callable[Concatenate[Self, P], None] # type: ignore
) -> Callable[Concatenate[Self, P], None]: # type: ignore
    """Decorator for call functions used to forward test instances

    Catches test successes and failures
    """
    def decorated(self: 'TestRunner', *args: P.args, **kwargs: P.kwargs) -> None:
        try:
            if not self._done:
                func(self, *args, **kwargs)
        except TestSuccess:
            self.endTest(True)
        except Exception as e:
            self.endTest(False, e)

    return decorated

class TestOutput:
    """Simple wrapper for test output
    """
    def __init__(self, case: TestCase, result: TestResult, error: Optional[Exception]) -> None:
        self.case = case
        self.result = result
        self.error = error

    def printout(self, full: bool = False) -> None:
        if self.result == PASSED:
            pass_str = "Passed"
        elif self.result == SKIPPED:
            pass_str = "Skipped"
        else:
            pass_str = f"Failed with error {self.error}"
        print(f"{self.case}: {pass_str}")
        if full and self.result == FAILED:
            if self.error is not None:
                try:
                    raise self.error
                except Exception as e:
                    print(sys.exc_info()[2])
            else:
                print("No exception info")

class TestRunner:
    """Manages tests and runs all tests
    """

    _current_test: TestCase

    def __init__(self) -> None:
        self._iterator = iter(MANAGER)
        self._num_passed = 0
        self._failed_details: list[TestOutput] = []
        self._skipped_details: list[TestOutput] = []
        self._done = False
        self.nextTest()

    def nextTest(self):
        """Move to the next test case
        """
        try:
            self._current_test = next(self._iterator)
            # If the minimum version is too low
            if (
                self._current_test.min_version != -1
            and self._current_test.min_version < general.getVersion()
            ):
                output = TestOutput(self._current_test, SKIPPED, None)
                self.printOutput(output)
                self._skipped_details.append(output)
                self.nextTest()
                return
            self.activate()
        except StopIteration:
            self._done = True
            self.printResults()

    def printOutput(self, test: TestOutput):
        """Print output of a test case

        Args:
            test (TestOutput): test to print
        """
        if config.PRINT_EACH_TEST:
            test.printout()
        else:
            print(test.result, end='', flush=True)

    def printResults(self):
        """Prints overall results of all tests
        """
        print()
        print("-"*50)
        print(f"Test Results")
        print("-"*50)
        print(f"From {len(MANAGER)} tests")
        print(f"{self._num_passed} passed")
        print(f"{len(self._failed_details)} failed")
        print(f"{len(self._skipped_details)} skipped")
        print("-"*50)
        for t in self._failed_details:
            t.printout(full=True)
            print("-"*50)
        for t in self._skipped_details:
            t.printout()
            print("-"*50)

    def endTest(self, passed: bool, error: Optional[Exception] = None):
        """Move to the next test case
        """
        result = PASSED if passed else FAILED
        output = TestOutput(self._current_test, result, error)
        if passed:
            self._num_passed += 1
        else:
            self._failed_details.append(output)

        self.printOutput(output)
        self.nextTest()

    #                             - Callbacks -
    ############################################################################

    @callWrapper
    def activate(self) -> None:
        """Activate a new test
        """
        self._current_test.activate()

    @callWrapper
    def onInit(self) -> None:
        """Called during FL Studio's OnInit() method

        Used to test cases during OnInit(). Unlike other test cases, this will
        be called once for each test when the script starts up. Care should be
        taken such that tests here don't interfere with other test cases.
        """
        self._current_test.onInit()

    @callWrapper
    def onMidiIn(self, event) -> None:
        """Called during FL Studio's OnMidiIn() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        self._current_test.onMidiIn(event)

    @callWrapper
    def onMidiMsg(self, event) -> None:
        """Called during FL Studio's OnMidiMsg() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onSysEx(self, event) -> None:
        """Called during FL Studio's OnSysEx() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onNoteOn(self, event) -> None:
        """Called during FL Studio's OnNoteOn() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onNoteOff(self, event) -> None:
        """Called during FL Studio's OnNoteOff() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onControlChange(self, event) -> None:
        """Called during FL Studio's OnControlChange() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onPitchBend(self, event) -> None:
        """Called during FL Studio's OnPitchBend() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onKeyPressure(self, event) -> None:
        """Called during FL Studio's OnKeyPressure() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onChannelPressure(self, event) -> None:
        """Called during FL Studio's OnChannelPressure() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onMidiOutMsg(self, event) -> None:
        """Called during FL Studio's OnMidiOutMsg() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onIdle(self) -> None:
        """Called during FL Studio's OnIdle() method

        Used to test cases during OnIdle()

        Args:
            event (EventData): event to test
        """
        ...

    @callWrapper
    def onRefresh(self, flags: int) -> None:
        """Called during FL Studio's OnRefresh() method

        Args:
            flags (int): refresh flags
        """

    @callWrapper
    def onDoFullRefresh(self) -> None:
        """Called during FL Studio's OnDoFullRefresh() method
        """

    @callWrapper
    def onUpdateBeatIndicator(self, value: int) -> None:
        """Called during FL Studio's OnUpdateBeatIndicator() method

        Args:
            value (int): beat type: 0 = Off; 1 = Bar; 2 = Beat
        """

    @callWrapper
    def onDisplayZone(self):
        """Called during FL Studio's OnDisplayZone() method
        """

    @callWrapper
    def onUpdateLiveMode(self, last_tracK: int):
        """Called during FL Studio's OnUpdateLiveMode() method
        """

    @callWrapper
    def onDirtyMixerTrack(self, index: int):
        """Called during FL Studio's OnDirtyMixerTrack() method
        """

    @callWrapper
    def onDirtyChannel(self, index: int, flag: int):
        """Called during FL Studio's OnDirtyChannel() method
        """

    @callWrapper
    def onFirstConnect(self):
        """Called during FL Studio's OnFirstConnect() method
        """

    @callWrapper
    def onUpdateMeters(self):
        """Called during FL Studio's OnUpdateMeters() method
        """

    @callWrapper
    def onWaitingForInput(self):
        """Called during FL Studio's OnWaitingForInput() method
        """

    @callWrapper
    def onSendTempMsg(self, message: str, duration: int):
        """Called during FL Studio's OnSendTempMsg() method
        """

