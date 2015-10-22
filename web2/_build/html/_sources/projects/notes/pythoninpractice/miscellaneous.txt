.. _miscellaneous:

====================
Miscellaneous Tips
====================

Measuring the execution time
----------------------------

to meausre how long a program runs, we could use ``time.clock()`` in ``time`` module

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 4, 5

   import time

   def time_execution(code):
       start = time.clock()
       result = eval(code)
       run_time = time.clock() - start
       return result, run_time

   def spin_loop(n):
       i = 0
       while i < n:
           i = i + 1

[4]:
    built-in procedure that provided by ``time`` module that evaluates to the number of seconds. 
    Often comes in pair, one sets the timer to start and one to stop the timer.

[5]:
    ``eval`` takes in a string, and evaluates it as python code.

output:

.. sourcecode:: ipython
   :linenos:

   In [1]: time_execution('1+1')
   Out[1]: (2, 0.0)

   In [2]: time_execution('spin_loop(10000000)')
   Out[2]: (None, 0.9900000000000002)   


