#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Trevor Kling
# Student ID: 002270716
# Email: kling109@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW09
###

###
# General Commends:
###

import numpy as np
import matplotlib.pyplot as plt

def gradient(x):
    """
    Computes the differential operator for a given set of points x.  This formulation uses the definition of gradient as a matrix, using matrix multiplication.  The program starts by initializing the array,
    filling all squares with 0's.  The rows are then defined based on where in x they fall. The front and back edges use the forward and backward difference respectively, while points in the middle are defined
    by the center difference.
    """
    dx = x[1] - x[0]
    newGrad = (((np.tri(len(x), len(x), 0) - np.tri(len(x), len(x), 1))) + (np.tri(len(x), len(x), -1) - np.tri(len(x), len(x), -2))) / (2*dx)
    newGrad[0][0] = -1 / dx
    newGrad[1][0] = 1 / dx
    newGrad[-1][-1] = 1 / dx
    newGrad[-2][-1] = -1 / dx
    return newGrad

def plot(x, func, funcName, gradName):
        """
        Graphs the given function as well as its derivative, using the gradient defined above.  Functions are graphed in black, while their derivative is graphed in red.  Both have their functions written on a
        legend in the top right hand corner.  Both functions are graphed over some range "x".  For the titles, .format was not used as it appears to cause issues with brackets used in latex formatting.
        """
        f = plt.figure(figsize=(16,12))
        a = plt.axes()
        funcGen = np.vectorize(func)
        y = funcGen(x)
        grad = gradient(x)
        derivative = y @ grad
        a.plot(x, y, label="$f(x) = $" + funcName, color='k')
        a.plot(x, derivative, label="$Df(x)=$" + gradName, color='r')
        a.set(xlabel="x", ylabel="y", title="Plot of " + funcName)
        a.legend()
        plt.show()