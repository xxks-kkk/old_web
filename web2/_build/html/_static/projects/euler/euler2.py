"""Solution to problem 2 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 03:21:10 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

# n is the nth term inside the Fibonacci sequence
# return the vaule of the nth term
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
	
# choose the subFib from the Fibonacci sequence based upon the given range
# return the sum of the even values between the startNum and endNum
def subFib(startNum,endNum):
	sum = 0
	n = 0
	cur = fib(n)
	while cur<= endNum:
		if startNum <= cur:
				if (cur % 2) == 0:
					sum = sum + cur
		n += 1
		cur = fib(n)
	return sum

print subFib(1,4000000)
