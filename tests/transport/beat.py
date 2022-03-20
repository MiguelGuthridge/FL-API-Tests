
import transport

from fltest import flTest, TestCase


@flTest()
class GetHWBeatLedState(TestCase):
    """Test that the return of getHWBeatLEDState() matches that given by
    OnUpdateBeatIndicator()"""
    idx = 0

    def activate(self) -> None:
        # Restart transport so we activate the beat indicator
        transport.start()

    def onUpdateBeatIndicator(self, value: int) -> None:
        state = transport.getHWBeatLEDState()
        assert value == state, f"{value} == {state}"
        self.idx += 1
        if self.idx == 8:
            transport.stop()
            self.markSuccess()
