
import plugins

from fltest import flSimpleTest, Raises
from tests.helpers import floatApproxEq

@flSimpleTest()
def testSetGetVST():
    """Setting and getting VST parameter values"""
    plugins.setParamValue(0.5, 0, 0)
    v = plugins.getParamValue(0, 0)
    assert floatApproxEq(0.5, v), f"{v=} == 0.5"

@flSimpleTest()
def testSetGetFL():
    """Setting and getting FL parameter values"""
    plugins.setParamValue(0.5, 0, 1)
    v = plugins.getParamValue(0, 1)
    assert floatApproxEq(0.5, v), f"{v=} == 0.5"
