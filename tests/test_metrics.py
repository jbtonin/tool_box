import numpy as np
from tool_box.metrics import rmsle

def test_rmsle():
    assert type(rmsle([4,4],[3,2])) == np.float64
    