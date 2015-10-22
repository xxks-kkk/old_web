"""Solution to problem 1 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 17:33:20 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

num = 0
sum = 0
while (num<1000):
	if (num % 3) == 0:
		sum = num + sum
	elif (num % 5) == 0:
		sum = num + sum
	num += 1

print sum
