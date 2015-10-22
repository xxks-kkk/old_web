.. _list_properties:

===========================================
Investigating Adding and Appending to Lists
===========================================

.. _adding_appending:

0. ``+`` and ``append``
-----------------------

0.1. same behavior?
*******************

Example 0. ``+`` and ``append`` do the same thing

.. sourcecode:: ipython
   :emphasize-lines: 3

   In [1]: list1 = [1, 2, 3, 4]

   In [2]: list1 = list1 + [5]

   In [3]: print list1
   [1, 2, 3, 4, 5]

.. sourcecode:: ipython
   :emphasize-lines: 3

   In [4]: list2 = [1, 2, 3, 4]

   In [5]: list2.append(5)

   In [6]: print list2
   [1, 2, 3, 4, 5]

[2] & [4]:
    From these two lines of codes, they do the same thing: add one more element to the list

0.2. Then, what's the difference?
*********************************

Difference 1:
    * ``append`` mutates the lists.
    * ``list1 = list1 + [element]`` creates a new list

Example 1. Difference 1

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 2, 5
   
   def proc(mylist):
       mylist.append(6)

   def proc2(mylist):
       mylist  = mylist + [6]

.. sourcecode:: ipython
   :emphasize-lines: 6
    
   In [9]: print list1
   [1, 2, 3, 4, 5]

   In [10]: proc(list1)

   In [11]: print list1
   [1, 2, 3, 4, 5, 6]

.. sourcecode:: ipython
   :emphasize-lines: 6

   In [12]: print list2
   [1, 2, 3, 4, 5]

   In [13]: proc2(list2)

   In [14]: print list2
   [1, 2, 3, 4, 5]

[2] & [11]:
    ``append`` mutates the lists. So, even though there is no ``return`` statement in ``proc`` function,
    we could still see the mutation on ``list1``.

[5] & [14]:
    ``list1 = list1 + [6]`` creates a new list. So, if there is no ``return`` statement,
    the list ``[1, 2, 3, 4, 5, 6]`` only exists inside the function as a newly created list.
    That's why calling the variable outside of the function, it still prints ``[1, 2, 3, 4, 5]``.

Difference 2:
    * ``append`` can *only* add one object to the list. It cannot concatenate two lists.
    * ``+`` can concatenate two lists.

Example 2. Difference 2: append

.. sourcecode:: ipython
   :emphasize-lines: 1, 4

   In [15]: list2.append([7,8,9])

   In [16]: list2
   Out[16]: [1, 2, 3, 4, 5, 6, [7, 8, 9]]

[15] & [16]:
    So here, ``append`` add a list (``[7,8,9]``) as one element to the list. 
    It does not produce ``[1,2,3,4,5,6,7,8,9]``, which is the concatenation of two strings.

Example 3. Difference 2: +

.. sourcecode:: ipython
   :emphasize-lines: 1, 4

   In [17]: list1 = list1 + [7,8,9]

   In [18]: list1
   Out[18]: [1, 2, 3, 4, 5, 7, 8, 9]

[17] & [18]:
    ``+`` actually two lists: ``[1,2,3,4,5,6]`` and ``[7,8,9]`` to form a new list ``[1,2,3,4,5,6,7,8,9]``

.. _+=:

1. ``+=``
---------

Example 4. ``+=`` works the same as ``append`` I

.. sourcecode:: ipython
   :linenos:
   :emphasize-lines: 3, 6

   In [19]: list3 = [1,2,3,4]

   In [20]: list3 += [5]

   In [21]: list3
   Out[21]: [1, 2, 3, 4, 5]

[19] & [21]:
    Here, ``+=`` works the same as ``append``: add ``5`` to the end of the list


Example 5. ``+=`` works the same as ``append`` II

.. sourcecode:: python
   :linenos:

   def proc3(mylis):
       mylist += [6]

.. sourcecode:: ipython
   :emphasize-lines: 6

   In [23]: print list3
   [1, 2, 3, 4, 5]

   In [24]: proc3(list3)

   In [25]: print list3
   [1, 2, 3, 4, 5, 6]

[25]: 
    so ``+=`` works the same as ``append``: it mutates the original list.

Example 6. ``+=`` concatenates the lists 

.. sourcecode:: ipython

   In [26]: list3 += [7,8,9]

   In [27]: list3
   Out[27]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   
2. Summary
----------

In terms of mutation of the list:
    * ``append`` and ``+=`` mutates the list.
    * ``+`` does not mutate the original list. Instead, it creates a new list.

In terms of modifying the list:
    * ``append`` only add element to the list. It cannot concatenate the list.
    * ``+`` and ``+=`` can concatenate the list.
