.. _indice:

=================================
Understanding Indices and Slicing
=================================

List or string indices are powerful techniques to help you 
quickly manipulate lists or strings.

**Applied Fields**

* String Slicing
* List indexing
* Setting ranges

.. _formats_slicing:

0. Formats in slicing
---------------------

Example 0 Setting

.. sourcecode:: python
    
   a = '0123456789' # where the char at k-th position is k

.. admonition:: Key Expression
   
   ::

    # slicing format
    b = a[start:stop:step]

There are only three things to remember:

    * ``start`` is the first item that *you want*
    * ``stop`` is the first item that you do *not* want
    * ``step``, being positive or negative, defines moving direction:

        - positive:

            moving forwards (from the first position of the string towards its end)

        - negative:

            moving backwards (from the last position of the str towards its start)

.. _indexing_pos_neg:

1. Indexing with positive and negative numbers
----------------------------------------------

1.0. with positive numbers
**************************

.. sourcecode:: python

   # counting from the beginning of the string starting at 0
   
   b = "my mistress' eyes are nothing like the sun"
        ^         ^                              ^
        b[0]     b[10]                           b[41]

1.1. with negative numbers
**************************

Sometimes it is useful to refer to chars of the string as seen from the end of the string.
In this case, we use negative numbers and count backwards, from -1 (*not from 0*)

.. sourcecode:: python
    
   # counting from the end of the string starting at -1

   b = "my mistress' eyes are nothing like the sun"
        ^         ^                              ^
        b[-42]    b[-32]                         b[-1]

1.2.connection
**************

In general, indexing with positive numbers and indexing with negative numbers have the following relation:

.. sourcecode:: python

   b[k] = b[-len(b)+k]

Example 1 connection with two indexing systems

.. sourcecode:: python

   len(b) = 42

   b[0]        = b[-len(b)] = b[-42] = 'm'
   b[len(b)-1] = b[-1]      = b[41]  = 'n'
   b[10]       = b[-32]              = 's'

.. _moving:

2. Moving
---------

2.0. Moving forwards
********************

**If step is positive we are moving forwards (if the value of 'step' is omitted, it defaults to +1)**

.. sourcecode:: python

   # the first char that we want is that in the 2nd position, 
   # the first char that we do not want is that in the 6th position

   a[2:6] = '0123456789'[2:6] = '2345'

Alternatively, seeing it from the end of the string:

.. sourcecode:: python
     
   # the first char that we want is that in the 8-th position from the end (i.e., the 2),
   # the first char that we do not want is that in the 4-th position from the end (i.e., the 6)

   a[-8:-4] = '0123456789'[-8:-4:1] = '2345'

Hence, for any positive step we have the following defaults:

.. sourcecode:: python

        |-> -> ->|
   a = '0123456789'
        ^        ^
    start:0    stop: len(a), i.e., one position beyond the end of the string

Thus::

    a[:]   = a[0:len(a):1] = '0123456789' # a +1 step is the default
    a[::2] = a[0:len(a):2] = '02468'      # all the even positions
    a[1::2] = '13579'                     # all the odd positions
    a[::3] = '0369'                       # all the multiples of 3

So, as long as you are starting or ending your slice with the start or the end of the string, you can
leave those out and Python will use the defaults.

2.1 Moving backwards
********************

**If step is negative then we are moving backwards**

.. sourcecode:: python

   # the first char that we want is that in the 6-th position,
   # the first char that we do not want is that in the 2nd position

   a[6:2:-1] = '0123456789'[6:2:-1] = '6543'

Alternatively,

.. sourcecode:: python

   # the first char that we want is that in the 4-th position from the back (i.e., the 6)
   # the first chat that we do not want is that in the 8-th position from the back (i.e., the 2)
   a[-4:-8:-1] = '0123456789'[-4:-8:-1] = '6543'

Notice that we can use positive or negative indices going either forwards or backwards on the string.. we 
can even mix them:

.. sourcecode:: python

   a[6:-8:-1] = '6543'
   a[-4:2:-1] = '6543'

Sometimes this mixing might come very handy:

.. sourcecode:: python
    
   url = '<a href="http://udacity.com">'[9:-2]
       = 'http://udacity.com'

.. note::

   Using negative Indices does not mean that we are moving backwards, 
   only that we are indexing from the end. 
   Moving forwards or backwards is determined solely by the 
   sign of the step variable.

Hence, for any negative steps, we have the following in mind:

.. sourcecode:: python
        
        |<- <- <-|
   a = '0123456789'
        ^        ^
        ^      start: -1
        stop: one position before the start of the string

hence:

.. sourcecode:: python
    
   a[::-1] = a[-1::-1] = '9876543210' # this is how we reverse a string in python
   a[::-2] = a[-1:-len(a)-1:-2] = '97531'
   a[::-3] = a[-1:-len(a)-1:-3] = '9630'

So now, we have mastered Python indices and should be able to understand:

.. sourcecode:: python

   '0123456789'[8:2:-2] = '864'
   '0123456789'[8:-8:-2] = '864'
   '0123456789'[-2:2:-2] = '864'
   '0123456789'[-2:-8:-2] = '864'
