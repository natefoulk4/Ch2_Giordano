"""Tests basics functionality and calculate module contained in
Ch2_Giordano/noDrag.py
"""

import pytest
from code.noDrag import calculate

"""Tests negative or zero angle of elevation"""
def test_strange_inputs():

    assert (0,0,0,0,0) == calculate(0,0,0,-10,0)

