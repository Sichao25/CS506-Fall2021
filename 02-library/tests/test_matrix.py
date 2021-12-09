# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:19:49 2021

@author: Sichao
"""

import pytest
import numpy as np

from cs506 import matrix

def test_matrix():
    assert matrix.get_determinant(np.asarray([[1, 1], [1, 1]])) == 0
    assert matrix.get_determinant(np.asarray([[1, 2], [2, 1]])) == -3