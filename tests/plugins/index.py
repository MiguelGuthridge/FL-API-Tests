
import plugins

from fltest import flSimpleTest, Raises

@flSimpleTest(unsafe=True)
def invalidParamNameIndex():
    """We shouldn't be able to access illegal param indexes"""
    with Raises(TypeError):
        plugins.getParamName(5000, 1)
