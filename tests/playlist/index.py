"""
tests > playlist > index

Tests for indexing of playlist
"""

from fltest import flSimpleTest

import playlist

@flSimpleTest()
def minIndex():
    """Access index 1"""
    playlist.getTrackName(1)

@flSimpleTest()
def maxIndex():
    """Access index 500"""
    playlist.getTrackName(500)
