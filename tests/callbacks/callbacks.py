
import device

from fltest import flTest, TestCase

def eventToInt(event) -> int:
    return event.status + (event.data1 << 8) + (event.data2 << 16)

@flTest()
class OnIdleCalled(TestCase):
    """Test that OnIdle() is being called correctly"""

    def onIdle(self) -> None:
        self.markSuccess()

@flTest()
class OnMidiIn(TestCase):
    """Test that OnMidiIn() is being called correctly"""

    def activate(self) -> None:
        # Send a MIDI message, which will be looped back to the device
        device.midiOutMsg(0x7F3C90)

    def onMidiIn(self, event) -> None:
        event.handled = True
        self.markSuccess()

@flTest()
class OnMidiMsgSysex(TestCase):
    """Test that OnMidiMsg() and OnSysEx() are called correctly"""

    standard = 0x7F3C90
    sysex = bytes([0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7])

    def activate(self) -> None:
        # Standard event
        device.midiOutMsg(self.standard)
        # Sysex event
        device.midiOutSysex(self.sysex)

    def onMidiMsg(self, event) -> None:
        assert event.sysex is None
        assert self.standard == eventToInt(event)
        event.handled = True
        self.markSuccess()

    def onSysEx(self, event) -> None:
        assert event.sysex == self.sysex
        event.handled = True
        self.markSuccess()

@flTest()
class OnNoteOn(TestCase):
    """Test that OnNoteOn() is being called correctly"""

    def activate(self) -> None:
        # Send a MIDI message, which will be looped back to the device
        device.midiOutMsg(0x7F3C90)

    def onNoteOn(self, event) -> None:
        event.handled = True
        self.markSuccess()

@flTest()
class OnNoteOff(TestCase):
    """Test that OnNoteOff() is being called correctly"""

    def __init__(self) -> None:
        super().__init__()
        self._count = 0

    def activate(self) -> None:
        # Send a MIDI message, which will be looped back to the device
        device.midiOutMsg(0x003C80)
        device.midiOutMsg(0x003C90) # Note off (note on at velocity=0)
        device.midiOutMsg(0x7F3C80)

    def onNoteOff(self, event) -> None:
        event.handled = True
        self._count += 1
        if self._count >= 3:
            self.markSuccess()

    def onNoteOn(self, event) -> None:
        event.handled = True
        self.markFailure(f"Registered as note on: 0x{eventToInt(event):06X}")
