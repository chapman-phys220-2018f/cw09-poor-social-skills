#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Trevor Kling
# Student ID: 002270716
# Email: kling109@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW09
###

import array_calculus as ac
import numpy as np

def test_gradient():
    """
    Tests that the gradient returns the correct value for a small range of values.
    """
    testx = np.arange(0, 5, 1)
    assert np.array_equal(ac.gradient(testx), np.array([[-1, -0.5, 0, 0, 0],[1, 0, -0.5, 0, 0], [0, 0.5, 0, -0.5, 0], [0, 0, 0.5, 0, -1], [0, 0, 0, 0.5, 1]]))
