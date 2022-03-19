"""
tests > transport > basic_transport

Tests for basic transport functions (playback, recording, etc)
"""

from fltest import flSimpleTest

import transport

@flSimpleTest()
def playback():
    state = bool(transport.isPlaying())
    transport.start()
    assert bool(transport.isPlaying()) != state
    transport.stop()
