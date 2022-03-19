#name=API Unit Tests

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

def OnIdle(self) -> None:
    runner.onIdle()

def OnRefresh(flags: int) -> None:
    runner.onRefresh(flags)

def OnDoFullRefresh(self) -> None:
    runner.onDoFullRefresh()

def OnUpdateBeatIndicator(value: int) -> None:
    runner.onUpdateBeatIndicator(value)

def OnDisplayZone(self):
    runner.onDisplayZone()

def OnUpdateLiveMode(last_tracK: int):
    runner.onUpdateLiveMode(last_tracK)

def OnDirtyMixerTrack(index: int):
    runner.onDirtyMixerTrack(index)

def OnDirtyChannel(index: int, flag: int):
    runner.onDirtyChannel(index, flag)

def OnFirstConnect(self):
    runner.onFirstConnect()

def OnUpdateMeters(self):
    runner.onUpdateMeters()

def OnWaitingForInput(self):
    runner.onWaitingForInput()

def OnSendTempMsg(message: str, duration: int):
    runner.onSendTempMsg(message, duration)
