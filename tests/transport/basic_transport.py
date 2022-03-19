"""
tests > transport > basic_transport

Tests for basic transport functions (playback, recording, etc)
"""

from fltest import flSimpleTest

import time
import transport

@flSimpleTest()
def playback():
    """Pressing play"""
    state = bool(transport.isPlaying())
    transport.start()
    assert bool(transport.isPlaying()) != state
    transport.stop()

@flSimpleTest()
def stop():
    """Pressing stop"""
    transport.start()
    transport.stop()
    assert not transport.isPlaying()

@flSimpleTest()
def playPosition():
    """Does pressing stop reset our playback position
    """
    transport.stop()
    transport.start()
    time.sleep(0.1)
    transport.start()
    assert transport.getSongPos() != 0.0

@flSimpleTest()
def stopPosition():
    """Does pressing stop reset our playback position
    """
    transport.start()
    time.sleep(0.1)
    transport.stop()
    assert transport.getSongPos() == 0.0

@flSimpleTest()
def record():
    """Pressing record"""
    state = bool(transport.isRecording())
    transport.record()
    assert bool(transport.isRecording()) != state
    transport.record()
    assert bool(transport.isRecording()) == state

@flSimpleTest()
def loop():
    """Loop mode"""
    state = transport.getLoopMode()
    transport.setLoopMode()
    assert state != transport.getLoopMode()
    transport.setLoopMode()
    assert state == transport.getLoopMode()

@flSimpleTest()
def songPosition():
    """Song position"""
    transport.stop()
    transport.setSongPos(0.5)
    assert transport.getSongPos() == 0.5
    transport.stop()
