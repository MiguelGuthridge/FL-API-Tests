"""
tests > playlist > index

Tests for indexing of playlist
"""

from fltest import flSimpleTest, Raises

import playlist

@flSimpleTest()
def minIndex():
    """Access index 1"""
    playlist.getTrackName(1)

@flSimpleTest()
def maxIndex():
    """Access index 500"""
    playlist.getTrackName(500)

@flSimpleTest()
def lowerBounds():
    """Test accessing out of bounds index 0"""
    with Raises(TypeError):
        playlist.getTrackName(0)

@flSimpleTest()
def upperBounds():
    """Test accessing out of bounds index 501"""
    with Raises(TypeError):
        playlist.getTrackName(501)
