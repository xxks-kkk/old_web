.. _chap4.rst:

==========================
The power of Introspection
==========================

Introspection: 
    
    code looking at other modules and functions in memory as objects,
    getting information about them, and manipulating them.

.. _diving_in:

4.1. Diving In
--------------

Example 4.1. apihelper.py (download `here <../../../_static/projects/notes/diveintopython/py/apihelper.py>`_) 

.. See :download:`here <./py/apihelper.py>`

.. sourcecode:: python

   # info takes any object that has functions or methods (like a module, which has 
   # functions, or a list,which has methods) and prints out the functions and their doc
   # strings.

   # collapse: multi-line doc strings are collapsed into a single long line ( if collapse == 1)
   # spacing: adjust the display of function names to make it easy to read

   def info(object, spacing=10, collapse=1):
   """Print methods and doc strings.

   Takes module, class, list, dictionary, or string."""
	   methodList = [e for e in dir(object) if callable(getattr(object, e))]
	   processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	   print "\n".join(["%s %s" % (method.ljust(spacing),processFunc(str(getattr(object, method).__doc__)))
                           for method in methodList])

   if __name__ == "__main__":
       print help.__doc__



Example 4.2 Sample Usage of apihelper.py

.. sourcecode:: ipython

   In [18]: from apihelper import info

   In [20]: li = []

   In [21]: info(li)
   append     L.append(object) -- append object to end
   count      L.count(value) -> integer -- return number of occurrences of value
   extend     L.extend(iterable) -- extend list by appending elements from the iterable
   index      L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.
   insert     L.insert(index, object) -- insert object before index
   pop        L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
   remove     L.remove(value) -- remove first occurrence of value. Raises ValueError if the value is not present.
   reverse    L.reverse() -- reverse *IN PLACE*
   sort       L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*; cmp(x, y) -> -1, 0, 1

Example 4.3 Advanced Usage of apihelper.py

.. sourcecode:: ipython

   In [25]: import odbchelper

   In [26]: info(odbchelper)
   buildConnectionString Build a connection string from a dictionary Returns string.

   In [28]: info(odbchelper, 30)
   buildConnectionString          Build a connection string from a dictionary Returns string.

   In [29]: info(odbchelper, 30, 0)
   buildConnectionString          Build a connection string from a dictionary
        
           Returns string.

.. _arguments:

4.2. Using Optional and Named Arguments
---------------------------------------

Python allows function arguments to have default values

* if the function is called without the argument, the argument gets its default value.
* arguments can be specified in any order by using named arguments.

Example 4.4.a  example of info

.. sourcecode:: python

    # spacing and collapse are optional (they have default values defined)
    # object is required (it has no default value)
    def info (object, spacing=10, collapse=1);

Example 4.4.b Valid Calls of info

::

    # With only one argument (object), spacing defaults to 10 and collapse defaults to 1.
    info(odbchelper)

    # With two arguments, collapse gets its default value of 1.
    info(odbchelper, 12)

    # here you are naming the collapse argument explicitly and specifying its value.
    # spacing still gets its default value of 10
    info(odbchelper, collapse=0)

    # Required arguments (i.e., object) can be named, and named arguments can appear in any order
    info(spacing=15, object=odbchelper)
    
* Arguments are simply a dictionary. The "normal" method of calling functions without argument names is
  actually just a shorthand where Python matches up the values with the argument names in the order
  they are specified in the function of declaration.

4.3. Built-in Functions
-----------------------

key funcs

::
    
    type(object), str(object), dir(object), callable(object)

4.3.1 **type** Function
***********************

* the **type** function returns the datatype of any arbitrary object.
* the possible types are listed in the types module.

Example 4.5 Introducing type

.. sourcecode:: ipython

   In [31]: type(1)
   Out[31]: int

   In [32]: li = []

   In [33]: type(li)
   Out[33]: list

   In [34]: import odbchelper

   In [35]: type(odbchelper)
   Out[35]: module

   In [36]: import types

   In [37]: type(odbchelper) == types.ModuleType
   Out[37]: True

* type takes anything and returns its datatype. Integers, strings, lists, dictionaries, tuples, functions, classes, modules, even types are acceptable.
* You can use the constants in the types module to compare types of objects.

4.3.2 **str** Function
**********************

* The **str** coerces data into a string.
* Every datatype can be coerced into a string.

Example 4.6 Introducing str

.. sourcecode:: ipython

  In [40]: horsemen = ['war','pestilence','famine']

  In [41]: horsemen
  Out[41]: ['war', 'pestilence', 'famine']

  In [42]: horsemen.append('Powerbuilder')

  In [43]: str(horsemen)
  Out[43]: "['war', 'pestilence', 'famine', 'Powerbuilder']"   # str works on list

  In [44]: str(odbchelper)
  Out[44]: "<module 'odbchelper' from 'odbchelper.py'>"   # str works on modules

  In [45]: str(None)   # str works on None
  Out[45]: 'None' 

4.3.2 **dir** Function
**********************

* The **dir** returns a list of the attributes and methods of any object: modules, functions, strings, lists, dictionaries, ...

Example 4.7 Introducing dir

.. sourcecode:: ipython
   
   In [47]: li = []

   In [48]: dir(li)
   Out[48]: ['__add__',
             '__class__',
             '__contains__',
             '__delattr__',
             '__delitem__',
             '__delslice__',
             '__doc__',
             '__eq__',
             '__format__',
             '__ge__',
             '__getattribute__',
             '__getitem__',
             '__getslice__',
             '__gt__',
             '__hash__',
             '__iadd__',
             '__imul__',
             '__init__',
             '__iter__',
             '__le__',
             '__len__',
             '__lt__',
             '__mul__',
             '__ne__',
             '__new__',
             '__reduce__',
             '__reduce_ex__',
             '__repr__',
             '__reversed__',
             '__rmul__',
             '__setattr__',
             '__setitem__',
             '__setslice__',
             '__sizeof__',
             '__str__',
             '__subclasshook__',
             'append',
             'count',
             'extend',
             'index',
             'insert',
             'pop',
             'remove',
             'reverse',
             'sort']
   
   In [51]: import odbchelper

   In [52]: dir(odbchelper)
   Out[52]: ['__author__',
             '__builtins__',
             '__copyright__',
             '__date__',
             '__doc__',
             '__file__',
             '__license__',
             '__name__',
             '__package__',
             '__version__',
             'buildConnectionString']

4.3.3 **callable** Function
***************************

* the **callable** function takes any object and returns True if the object can be called, or False otherwise.
* Callable objects include functions, class methods, even classes themselves.

Example 4.8 Introducing callable

.. sourcecode:: ipython

   In [54]: import string

   In [55]: string.punctuation
   Out[55]: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

   In [56]: string.join
   Out[56]: <function string.join>

   In [57]: callable(string.punctuation)
   Out[57]: False

   In [58]: callable(string.join)
   Out[58]: True

   In [59]: print string.join.__doc__
   join(list [,sep]) -> string

       Return a string composed of the words in list, with
       intervening occurrences of sep.  The default separator is a
       single space.

       (joinfields and join are synonymous)

.. admonition:: usage of callable

   By using the callable function on each of an object's attributes, you can determine which attributes you care about (methods, functions, classes)
   and which you want to ignore (constants and so on) without knowing anything about the object ahead of time.

4.3.4 Built-in Functions
************************

* type, str, dir, and all the rest of Python's built-in functions are grouped into a special module called __builtin__

Example 4.9 Built-in Attributes and Functions

.. sourcecode:: ipython

   In [60]: from apihelper import info

   In [61]: import __builtin__

   In [62]: info(__builtin__,20)
   ArithmeticError      Base class for arithmetic errors.
   AssertionError       Assertion failed.
   AttributeError       Attribute not found.
   BaseException        Common base class for all exceptions
   BufferError          Buffer error.

   [...skip...]

.. _getattr:

4.4. Getting Object References With getattr
-------------------------------------------

key func

.. sourcecode:: python

   getattr(object, attr)

**getattr** allows you to get a reference to a function

Example 4.10 Introducing getattr

.. sourcecode:: ipython

   In [63]: li = ["Larry","Curly"]

   In [64]: li.pop
   Out[64]: <function pop>

   In [65]: getattr(li,"pop")
   Out[65]: <function pop>

   In [66]: getattr(li,"append")("Moe")

   In [67]: li
   Out[67]: ['Larry', 'Curly', 'Moe']

   In [68]: getattr({},"clear")
   Out[68]: <function clear>

   In [69]: getattr((),"pop")
   ---------------------------------------------------------------------------
   AttributeError                            Traceback (most recent call last)
   <ipython-input-69-e1701c6ecc00> in <module>()
   ----> 1 getattr((),"pop")

   AttributeError: 'tuple' object has no attribute 'pop'

* [64]: this gets a reference to the pop method of the list. Note that this is not calling the pop method; that would be li.pop(). 

* [65]: This also returns a reference to the pop method, but this time, the method name is specified as a string argument to the getattr function.

* [65]: getattr returns any attribute of any object. In this case, the object is a list, and the attribute is the pop method.

* [66]: getattr(x,y) == x.y . In this case, getattr(li,"append")("Moe") == li.append("Moe")

4.4.1 getattr with Modules
**************************

Example 4.11 The getattr Function in apihiper.py

.. sourcecode:: ipython

   In [71]: import odbchelper

   In [72]: odbchelper.buildConnectionString
   Out[72]: <function odbchelper.buildConnectionString>

   In [73]: getattr(odbchelper,"buildConnectionString")
   Out[73]: <function odbchelper.buildConnectionString>

   In [74]: object = odbchelper

   In [75]: method = "buildConnectionString"

   In [76]: getattr(object,method)
   Out[76]: <function odbchelper.buildConnectionString>

   In [77]: type(getattr(object,method))
   Out[77]: function

   In [78]: import types

   In [80]: type(getattr(object, method)) == types.FunctionType
   Out[80]: True

   In [81]: callable(getattr(object,method))
   Out[81]: True

* Using getattr, you can get the same reference to the same function. 
  In general, getattr(object,"attribute") is equivalent to object.attribute.
  If object is a module, then attribute can be anything defined in the module: a function, class, or global variable.

4.4.2. getattr As a Dispatcher
******************************

.. admonition:: idea

   For example, if you had a program that could output data in a variety of different formats, you could define separate
   functions for each output format and use a single dispatch function to call the right one.


Let's imagine a program that prints site statisticss in HTML, XML, and plain text formats. The choice of output format
could be specified on the command line, or stored in a configuration file. A *statsout* module defines three functions,
*output_html*, *output_xml*, and *output_text*. Then the main program defines a single output function:

Example 4.12 Creating a Dispatcher with getattr

::
    
    import statsout
    
    # output function takes one required argument, data, and one optional argument, format.
    # if format is not specified, it defaults to text
    def output(data, format="text"):
        output_function = getattr(statsout, "output_%s" % format)
        return output_function(data)

.. admonition:: advantage

   This allows you to easily extend the program later to support other output formats, without changing this dispatch
   function. Just add another function to *statsout* named, for instance, *output_pdf*, and pass "pdf" as the format into
   the output function.

.. admonition:: bug

   There is no error checking.
   What happends if the user passes in a format that doesn't have a corresponding function defined in *statsout*?
   Well, *getattr* will return None, which will be assigned to output_function instead of a valid function, and
   next line that attempts to call that function will crash and raise an exception. That's bad.

.. admonition:: solution

   *getattr* takes an optional third argument, a default value.

Example 4.13 getattr Default Values

::

    import statsout

    def output(data, format="text"):
        
        # The third argument (i.e., statsout.output_text) is a default value
        # that is returned if the attribute or method specified by the second argument wasn't found.
        output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
        return output_function(data)

.. _filter_list:

4.5. Filtering Lists
--------------------

a filtering mechanism, where some elements in the list are mapped while others are skipped entirely.

.. admonition:: list filtering syntax

   ::

        # any element for which the filter expression evaluates true will be included in the mapping.
        # All other elements are ignored,
        # so they are never put through the mapping expression and are not included in the output list.
        [mapping-expression for element in source-list if filter-expression]


Example 4.14 Introducing List Filtering

.. sourcecode:: ipython

   In [1]: li = ["a","mpilgrim","foo","b","c","b","d","d"]

   In [2]: [elem for elem in li if len(elem) > 1]
   Out[2]: ['mpilgrim', 'foo']

   In [3]: [elem for elem in li if elem != "b"]
   Out[3]: ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']

   In [4]: [elem for elem in li if li.count(elem) == 1]
   Out[4]: ['a', 'mpilgrim', 'foo', 'c'] 

* [4]: filter would not eliminate duplicates from a list.

.. admonition:: mechanism
   
   The mapping expression in the previous example is simple (it just returns the value of each element).
   As Python loops through the list, it runs each element through the filter expression. If the filter
   expression is true, the element is mapped and the result of the mapping expression is included in the
   returned list.

.. _ and, or:

4.6. The Peculiar Nature of **and** and **or**
----------------------------------------------

**and** and **or** perform boolean logic, but they do not return boolean values; instead, they return one of the actual values they are comparing.

Example 4.15 Introducing and

.. sourcecode:: ipython

   In [1]: 'a' and 'b'
   Out[1]: 'b'

   In [2]: '' and 'b'
   Out[2]: ''

   In [3]: 'a' and 'b' and 'c'
   Out[3]: 'c'

* If all values are true in a boolean context, **and** returns the last value.
* If any value is false in a boolean context, **and** returns the first false value.

Example 4.16 Introducing or

.. sourcecode:: ipython

   In [5]: 'a' or 'b'
   Out[5]: 'a'

   In [6]: '' or 'b'
   Out[6]: 'b'

   In [7]: '' or [] or {}
   Out[7]: {}

   In [8]: def sidefx():
      ...:     print "in sidefx()"
      ...:     return 1

   In [9]: 'a' or sidefx()
   Out[9]: 'a'

* If any value is true, **or** returns that value immediately.
  ( **or** evaluates values only until it finds one that is true in a boolean context, and then it ignores the rest.)

* If all values are false, **or** returns the last value.

4.6.1 Using the and-or Trick
****************************

.. admonition:: usage

   * simplify the syntax
   * some cases in Python where if statements are not allowed (i.e., lambda functions)

.. admonition:: Analogy with C
   
   C:

   .. code-block:: c
        
      /* expression evaluates to a if bool is true, and b otherwise*/  
      bool ? a : b

   Python:

   .. code-block:: python

      # expression evaluates to a if (bool and a) is true, and b otherwise
      # requires a to be True
      bool and a or b

Example 4.17 Introducing the and-or Trick

.. sourcecode:: ipython

  In [11]: a = "first"

  In [12]: b = "second"

  In [13]: 1 and a or b
  Out[13]: 'first'

  In [14]: 0 and a or b
  Out[14]: 'second' 

.. admonition:: bug

   If the value of a is false, the expression will not works as you would expect it to. In other words,
   The and-or trick, bool and a or b, will not work like the C expression bool ? a : b when a is false in boolean context

Example 4.18 When the and-or Trick Fails

.. sourcecode:: ipython

   In [15]: a = ""

   In [16]: b = "second"

   In [17]: 1 and a or b
   Out[17]: 'second' 

.. admonition:: solution
    
   The real trick behind the and-or trick, then, is to make sure that the value of a is never false.
   One common way of doing this is to turn a into [a] and b into [b], then taking the first element of the returned list, which will be either a or b.

Example 4.19 Using the and-or Trick safely

.. sourcecode:: ipython

   In [18]: a = ""

   In [19]: b = "second"

   In [20]: (1 and [a] or [b])[0]
   Out[20]: '' 

* since [a] is a non-empty list, it is never false. Even if a is 0 or '' or some other false value, the list [a] is true because it has one element.

.. _lambda:

4.7 Using lambda Functions
--------------------------

Python supports an interesting syntax that lets you define one-line mini-functions on the fly.
Borrowed from Lisp, these so-called lambda functions can be used anywhere a function is required.

Example 4.20 Introducing lambda Functions

.. sourcecode:: ipython

   In [1]: def f(x):
      ...:     return x*2

   In [2]: f(3)
   Out[2]: 6

   In [3]: g = lambda x: x*2

   In [4]: g(3)
   Out[4]: 6

   In [5]: (lambda x: x*2)(3)
   Out[5]: 6
 
* [3]: This is a lambda function that accomplishes the same thing as the normal function above it.

* [3]: lambda function:
        
        - function that takes any number of arguments (including optional arguments) and returns the value of a single expression
        - lambda functions cannot contain commands
        - cannot contain more than one expression
        - no parentheses around the argument list
        - return keyword is missing (it is implied, since the entire function can only be one expression)
        - function has no name, but it can be called through the variable it is assigned to

4.7.1 Real-World lambda Functions
*********************************

Here are the lambda functions in apihelper.py:

.. sourcecode:: python
  
   # processFunc is now a function, but which function it is depends on the value of the collapse variable.
   # If collapse is true, processFunc(string) will collapse whitespace; 
   # otherwise, processFunc(string) will return its argument unchanged

   processFunc = collapse and (lambda s: "".join(s.split())) or (lambda s:s)

Example 4.21 split With No Arguments

.. sourcecode:: ipython

  In [1]: s = "this   is\na\ttest"

  In [2]: print s
  this   is
  a       test

  In [3]: print s.split()
  ['this', 'is', 'a', 'test']

  In [5]: print " ".join(s.split())
  this is a test 

* [2]: This is a multiline string, defined by escape characters instead of triple quotes. \n is a carriage return, and \t is a tab character

* [3]: split without any arguments splits on whitespace. So three spaces, a carriage return, and a tab character are all the same.

* [5]: You can normalize whitespace by splitting a string with split and then rejoining it with join, using a single space as a delimiter.

* [5]: This is what the info function does to collapse multi-line doc strings into a single line.

.. _alltogether:

4.8 Putting It All Together
---------------------------

::
    
    print "\n".join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object,method).__doc__))) 
                    for method in methodList])

Example 4.22 Getting a doc string Dynamically

.. sourcecode:: ipython

   In [29]: import odbchelper

   In [30]: object = odbchelper

   In [31]: method = 'buildConnectionString'

   In [32]: getattr(object,method)
   Out[32]: <function odbchelper.buildConnectionString>

   In [33]: print getattr(object,method).__doc__
   Build a connection string from a dictionary
        
           Returns string.

Example 4.23 Why Use str on a doc string?

.. sourcecode:: ipython

   In [35]: def foo(): print 2

   In [36]: foo()
   2

   In [37]: foo.__doc__

   In [38]: foo.__doc__ == None
   Out[38]: True

   In [39]: str(foo.__doc__)
   Out[39]: 'None'

* reason: processFunc is assuming a string argument and calling its split method, which would crash if you passed it None
  because None doesn't have a split method.

Example 4.24 Introducing ljust

.. sourcecode:: ipython

   In [41]: s = 'buildConnectionString'

   In [42]: s.ljust(30)
   Out[42]: 'buildConnectionString         '

   In [43]: s.ljust(20)
   Out[43]: 'buildConnectionString'

::

    # pads the string with spaces to the given length. 
    # if the given length is smaller than the length of the string, ljust will simply return the string unchanged.
    # it never truncates string,
    string.ljust(length)

* This is what the info function uses to make two columns of output and line up all the doc strings in the second column.

Example 4.25 Printing a List

.. sourcecode:: ipython
   
  In [44]: li = ['a','b','c']

  In [45]: print '\n'.join(li)
  a
  b
  c 
