
from testcase import TestCase, TestSuccess
from manager import TestManager

class TestRunner:
    _current_test: TestCase
    def __init__(self) -> None:
        self._iterator = TestManager.
        self._current_test = None

    def callWrapper(self, *args, **kwargs):
        """Decorator for call functions used to forward test instances

        Catches test successes and failures
        """

    #                             - Callbacks -
    ############################################################################

    def activate(self) -> None:
        """Activate a new test
        """
        ...

    def onInit(self) -> None:
        """Called during FL Studio's OnInit() method

        Used to test cases during OnInit(). Unlike other test cases, this will
        be called once for each test when the script starts up. Care should be
        taken such that tests here don't interfere with other test cases.
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

