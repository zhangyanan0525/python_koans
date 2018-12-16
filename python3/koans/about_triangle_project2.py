#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        # All sides should be greater than 0
            triangle(4, 4, 4)
            triangle(3, 4, 4)

        # The sum of any two sides should be greater than the third one
            triangle(4,4, 3)
            triangle(4, 5, 4)


