#name=API Unit Tests

# Enable static typing features
import fl_typing

# Load tests
import tests

# And finally create our test runner
from fltest import TestRunner
runner = TestRunner()

def OnInit() -> None:
    runner.onInit()

def OnMidiIn(event) -> None:
    runner.onMidiIn(event)

def OnMidiMsg(event) -> None:
    runner.onMidiMsg(event)

def OnSysEx(event) -> None:
    runner.onSysEx(event)

def OnNoteOn(event) -> None:
    runner.onNoteOn(event)

def OnNoteOff(event) -> None:
    runner.onNoteOff(event)

def OnControlChange(event) -> None:
    runner.onControlChange(event)

def OnPitchBend(event) -> None:
    runner.onPitchBend(event)

def OnKeyPressure(event) -> None:
    runner.onKeyPressure(event)

def OnChannelPressure(event) -> None:
    runner.onChannelPressure(event)

def OnMidiOutMsg(event) -> None:
    runner.onMidiOutMsg(event)

def OnIdle() -> None:
    runner.onIdle()

def OnRefresh(flags: int) -> None:
    runner.onRefresh(flags)

def OnDoFullRefresh() -> None:
    runner.onDoFullRefresh()

def OnUpdateBeatIndicator(value: int) -> None:
    runner.onUpdateBeatIndicator(value)

def OnDisplayZone():
    runner.onDisplayZone()

def OnUpdateLiveMode(last_tracK: int):
    runner.onUpdateLiveMode(last_tracK)

def OnDirtyMixerTrack(index: int):
    runner.onDirtyMixerTrack(index)

def OnDirtyChannel(index: int, flag: int):
    runner.onDirtyChannel(index, flag)

def OnFirstConnect():
    runner.onFirstConnect()

def OnUpdateMeters():
    runner.onUpdateMeters()

def OnWaitingForInput():
    runner.onWaitingForInput()

def OnSendTempMsg(message: str, duration: int):
    runner.onSendTempMsg(message, duration)
