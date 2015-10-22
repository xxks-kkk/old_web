.. _mutable:

=================================
Mutable Objects in Function Calls
=================================

Here, I showed the differences between mutable objects and immutable objects in terms of function call.

.. _setup:

0. Example Setup
----------------

Example 0 Mutable Objects in function Call

Here, the mutable object is list.

.. sourcecode:: python
   :linenos:

   # Define a procedure, replace_spy, that takes as its input a list of three numbers, 
   # and modifies the value of the third element in the input list to be one more than its previous value

   
   def replace_spy(p):
       p[2] = p[2] + 1


.. sourcecode:: python
   :linenos:

   # test
   spy = [0,0,7]
   replace_spy (spy)
   print spy

output::
    
    >>> [0,0,8]

Example 1 Immutable Objects in function Call 

.. sourcecode:: python
   :linenos:

   # Define a procedure, inc, that takes a number as input and increase that number by 1

   def inc(n):
        n = n + 1

.. sourcecode:: python
   :linenos:

   # test
   a = 3
   inc(a)
   print a

output::
    
    >>> 3
    
1. Comparison
-------------

.. sourcecode:: python

   # here is what happened in replace_spy (mutable object in function call)
        
        before 'p[2] = p[2] + 1' statement     after 'p[2] = p[2] + 1' statement

        +---+---+---+  <---- spy               +---+---+---+  <---- spy
        | 0 | 0 | 7 |  <---- p                 | 0 | 0 | 8 |  <---- p
        +---+---+---+                          +---+---+---+

When we call a function, the name of the variable in the function now refers to the object that's passed in.
So, now the value of ``P`` of the parameter here refers to that object. Then after ``p[2] = p[2] + 1`` statement,
since both ``p`` and ``spy`` refers to the same object, then modification in ``p`` also modifies the value in ``spy``.
This only works when the object is *mutable*.

.. sourcecode:: python

   # here is what happended in inc (immutable object in function call)

      before 'n = n + 1' statement          after 'n = n + 1' statement
      
      +---+   <---- a                      +---+  <--- a   +---+  <---- n
      | 3 |   <---- n                      | 3 |           | 4 |
      +---+                                +---+           +---+

Same as the mutable object, when we call a function, the name of the variable in the function now refers to the object 
tha's passed in. Son now the value of ``n`` of the para here refers to that object. Since the number is immutable object,
now ``n`` actually refers to a new object ``4``. Essentially, this function does nothing, ``a`` still be ``3``.


