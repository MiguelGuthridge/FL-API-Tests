
from typing import Callable, Optional, NoReturn
import config as config

TestFunction = Callable[[], None]

class TestSuccess(BaseException):
    """Raised when a test is successful
    """

class TestFailure(Exception):
    """Raised when a test has failed
    """

class TestCase:
    """Base class representing a single test case

    This is extended by the following classes to allow for simple test cases to
    be created:
    * SimpleTest
    """

    def __init__(
        self,
        name: Optional[str] = None,
        details: Optional[str] = None,
        min_version: int = -1,
        unsafe: bool = False
    ) -> None:
        if name is None:
            self.name = f"{self.__module__}.{self.__class__.__name__}"
        else:
            self.name = name

        if details is None:
            if self.__doc__ is not None:
                self.details = self.__doc__.strip()
            else:
                self.details = ""
        else:
            self.details = details.strip()
        self.min_version = min_version
        self.unsafe = unsafe

    def __repr__(self) -> str:
        if len(self.details):
            return f"{self.name} ({self.details})"
        else:
            return self.name

    def markSuccess(self) -> NoReturn:
        """Mark a multi-stage test case as completed
        """
        raise TestSuccess()

    def markFailure(self, reason: str) -> NoReturn:
        """Mark a multi-stage test case as failed
        """
        raise TestFailure(reason)

    #                             - Callbacks -
    ############################################################################

    def activate(self) -> None:
        """Called when this test starts running

        This can be used to perform any setup required to get the test ready,
        or for simple tests can just run the entire test.
        """
        ...

    def onMidiIn(self, event) -> None:
        """Called during FL Studio's OnMidiIn() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onMidiMsg(self, event) -> None:
        """Called during FL Studio's OnMidiMsg() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onSysEx(self, event) -> None:
        """Called during FL Studio's OnSysEx() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onNoteOn(self, event) -> None:
        """Called during FL Studio's OnNoteOn() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onNoteOff(self, event) -> None:
        """Called during FL Studio's OnNoteOff() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onControlChange(self, event) -> None:
        """Called during FL Studio's OnControlChange() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onPitchBend(self, event) -> None:
        """Called during FL Studio's OnPitchBend() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onKeyPressure(self, event) -> None:
        """Called during FL Studio's OnKeyPressure() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onChannelPressure(self, event) -> None:
        """Called during FL Studio's OnChannelPressure() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onMidiOutMsg(self, event) -> None:
        """Called during FL Studio's OnMidiOutMsg() method

        As tests must be triggered by using a loopback system, all events that
        we are expecting to process here must be sent out by this script.

        Args:
            event (EventData): event to test
        """
        ...

    def onIdle(self) -> None:
        """Called during FL Studio's OnIdle() method

        Used to test cases during OnIdle()

        Args:
            event (EventData): event to test
        """
        ...

    def onRefresh(self, flags: int) -> None:
        """Called during FL Studio's OnRefresh() method

        Args:
            flags (int): refresh flags
        """

    def onDoFullRefresh(self) -> None:
        """Called during FL Studio's OnDoFullRefresh() method
        """

    def onUpdateBeatIndicator(self, value: int) -> None:
        """Called during FL Studio's OnUpdateBeatIndicator() method

        Args:
            value (int): beat type: 0 = Off; 1 = Bar; 2 = Beat
        """

    def onDisplayZone(self):
        """Called during FL Studio's OnDisplayZone() method
        """

    def onUpdateLiveMode(self, last_tracK: int):
        """Called during FL Studio's OnUpdateLiveMode() method
        """

    def onDirtyMixerTrack(self, index: int):
        """Called during FL Studio's OnDirtyMixerTrack() method
        """

    def onDirtyChannel(self, index: int, flag: int):
        """Called during FL Studio's OnDirtyChannel() method
        """

    def onFirstConnect(self):
        """Called during FL Studio's OnFirstConnect() method
        """

    def onUpdateMeters(self):
        """Called during FL Studio's OnUpdateMeters() method
        """

    def onWaitingForInput(self):
        """Called during FL Studio's OnWaitingForInput() method
        """

    def onSendTempMsg(self, message: str, duration: int):
        """Called during FL Studio's OnSendTempMsg() method
        """

class SimpleTest(TestCase):
    """Represents a test that can be completed within a single function

    The function should be provided to the constructor
    """

    def __init__(
        self,
        test_case: TestFunction,
        min_version: int = -1,
        unsafe: bool = False
    ) -> None:
        test_name = f"{test_case.__module__}.{test_case.__name__}"
        details = test_case.__doc__
        if details is None:
            details = ""

        super().__init__(test_name, details, min_version, unsafe)
        self._test = test_case

    def activate(self) -> None:
        self._test()
        self.markSuccess()
