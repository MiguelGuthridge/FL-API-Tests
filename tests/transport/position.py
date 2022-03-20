"""
tests > transport > position

Tests for getting and setting transport positions
"""

from fltest import flSimpleTest, Raises

import transport

@flSimpleTest()
def positionDefault():
    transport.stop()
    # milliseconds
    assert transport.getSongPos(0) == 0, "ms"
    # Seconds
    assert transport.getSongPos(1) == 0, "s"
    # Abs ticks
    assert transport.getSongPos(2) == 0, "abs_ticks"
    # Bars
    assert transport.getSongPos(3) == 1, "bars"
    # Steps
    assert transport.getSongPos(4) == 1, "steps"
    # Ticks
    assert transport.getSongPos(5) == 0, "ticks"

@flSimpleTest()
def setPosMS():
    transport.stop()
    # Need to use specific value because of rounding with PPQN
    transport.setSongPos(196, 0)
    p = transport.getSongPos(0)
    assert p == 196, f"{p=} == 196"

@flSimpleTest()
def setPosSecs():
    transport.stop()
    transport.setSongPos(2, 1)
    p = transport.getSongPos(1)
    assert p == 2, f"{p=} == 2"

@flSimpleTest()
def setPosAbsTick():
    transport.stop()
    transport.setSongPos(2, 2)
    p = transport.getSongPos(2)
    assert p == 2, f"{p=} == 2"

@flSimpleTest()
def setPosBar():
    transport.stop()
    transport.setSongPos(2, 3)
    p = transport.getSongPos(3)
    assert p == 2, f"{p=} == 2"

@flSimpleTest()
def setPosStep():
    transport.stop()
    transport.setSongPos(2, 4)
    p = transport.getSongPos(4)
    assert p == 2, f"{p=} == 2"

@flSimpleTest()
def setPosTick():
    transport.stop()
    transport.setSongPos(2, 5)
    p = transport.getSongPos(5)
    assert p == 2, f"{p=} == 2"
