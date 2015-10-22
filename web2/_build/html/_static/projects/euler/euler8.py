"""Solution to problem 8 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 17:33:20 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"


import os

# open the file to read
f = open(os.path.abspath('euler8_input.txt'))
# store the 1000 digits
data = ''
# store the parse result from one line
parse = ''
# product of five consecutive digits (final result)
product = 0
# index
i = 0
# product of five consecutive digits (cal result)
result = 0

# parse the input file to form 1000 digits into one string
for line in f:
    # note line.strip('\n') will not affect 'line'
    parse = line.strip('\n')
    data = data + parse

while ((i+4) < len(data)):
    result = int(data[i]) * int(data[i+1]) * int(data[i+2]) * int(data[i+3]) * int(data[i+4])
    if result > product:
        product = result
    i += 1

print product
    
