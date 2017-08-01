# enums

from __future__ import division

import logging

logger = logging.getLogger(__name__)

# you can supply enum values as strings or ints ... these classes give the ints
# for each string, so pyvips.BandFormat.SHORT is equivalent to "short"

class BandFormat(object):
    UCHAR = 0
    CHAR = 1
    USHORT = 2
    SHORT = 3
    UINT = 4
    INT = 5
    FLOAT = 6
    COMPLEX = 7
    DOUBLE = 8
    DPCOMPLEX = 9

    def __eq__(self, other):
        print 'BANANA !!!'

class Interpretation(object):
	MULTIBAND = 0
	B_W = 1
	HISTOGRAM = 10
	XYZ = 12
	LAB = 13
	CMYK = 15
	LABQ = 16
	RGB = 17
	CMC = 18
	LCH = 19
	LABS = 21
	SRGB = 22
	YXY = 23
	FOURIER = 24
	RGB16 = 25
	GREY16 = 26
	MATRIX = 27
	SCRGB = 28
	HSV = 29