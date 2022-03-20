#name=API Unit Tests

# Enable static typing features
import fl_typing

from typing import Optional

from fltest import TestRunner
from fltest.manager import MANAGER

# Print out some basic info
print()
print("FL Studio API Tests")
print('-'*50)
print("Discovering tests...")
import tests
print(f"Found {len(MANAGER)} tests")
print('-'*50)
print("To run tests, open 'API Test Project.flp', then call the `run()` function")
print("To run unsafe tests too, call `run(unsafe=True)`")

runner: Optional[TestRunner] = None

def run(unsafe: bool = False):
    """Runs the tests"""
    global runner
    runner = TestRunner(unsafe)
    return ''

def OnMidiIn(event) -> None:
    if runner is not None:
        runner.onMidiIn(event)

def OnMidiMsg(event) -> None:
    if runner is not None:
        runner.onMidiMsg(event)

def OnSysEx(event) -> None:
    if runner is not None:
        runner.onSysEx(event)

def OnNoteOn(event) -> None:
    if runner is not None:
        runner.onNoteOn(event)

def OnNoteOff(event) -> None:
    if runner is not None:
        runner.onNoteOff(event)

def OnControlChange(event) -> None:
    if runner is not None:
        runner.onControlChange(event)

def OnPitchBend(event) -> None:
    if runner is not None:
        runner.onPitchBend(event)

def OnKeyPressure(event) -> None:
    if runner is not None:
        runner.onKeyPressure(event)

def OnChannelPressure(event) -> None:
    if runner is not None:
        runner.onChannelPressure(event)

def OnMidiOutMsg(event) -> None:
    if runner is not None:
        runner.onMidiOutMsg(event)

def OnIdle() -> None:
    if runner is not None:
        runner.onIdle()

def OnRefresh(flags: int) -> None:
    if runner is not None:
        runner.onRefresh(flags)

def OnDoFullRefresh() -> None:
    if runner is not None:
        runner.onDoFullRefresh()

def OnUpdateBeatIndicator(value: int) -> None:
    if runner is not None:
        runner.onUpdateBeatIndicator(value)

def OnDisplayZone():
    if runner is not None:
        runner.onDisplayZone()

def OnUpdateLiveMode(last_tracK: int):
    if runner is not None:
        runner.onUpdateLiveMode(last_tracK)

def OnDirtyMixerTrack(index: int):
    if runner is not None:
        runner.onDirtyMixerTrack(index)

def OnDirtyChannel(index: int, flag: int):
    if runner is not None:
        runner.onDirtyChannel(index, flag)

def OnFirstConnect():
    if runner is not None:
        runner.onFirstConnect()

def OnUpdateMeters():
    if runner is not None:
        runner.onUpdateMeters()

def OnWaitingForInput():
    if runner is not None:
        runner.onWaitingForInput()

def OnSendTempMsg(message: str, duration: int):
    if runner is not None:
        runner.onSendTempMsg(message, duration)

print("Ready")
print('-'*50)
