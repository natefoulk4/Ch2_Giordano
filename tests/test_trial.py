""" Tests mathy.py.
"""

import pytest

def test_square():
    """Tests the square function
    """
    from code.trial import square

    assert 4 == square(2)
