"""Solution to problem 9 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 23:45:15 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

# transform relations into ab = 1000(a+b)-500*1000
for a in range(0,1001):
    for b in range(0,1001):
        if (a*b == 1000*(a+b) - 500*1000):
            print a*b*(1000-a-b)
            break

