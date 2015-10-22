.. _chap3.rst:

================
Native Datatypes
================

.. _dictionaries:

3.1. Dictionaries
-----------------

dictionary: defines one-to-one relationships between keys and values

* Elements in dictionary are unordered.
* Keys are case-sensitive and have to be unique.
* Dictionary values can be any datatypes.

3.1.1 Defining Dictionaries
***************************

Example 3.1. Defining a Dictionary:

.. sourcecode:: ipython

   In [11]: d = {"server":"mpilgrim","database":"master"}  # create a dictionary
            
   In [12]: d
   Out[12]: {'database': 'master', 'server': 'mpilgrim'}

   In [13]: d["server"]
   Out[13]: 'mpilgrim'

   In [14]: d["database"]
   Out[14]: 'master'

   In [15]: d["mpilgrim"]
   ---------------------------------------------------------------------------
   KeyError                                  Traceback (most recent call last)
   <ipython-input-15-55e1c8e1e8e7> in <module>()
   ----> 1 d["mpilgrim"]

   KeyError: 'mpilgrim'

* *'server'* is a key, and its associated value, refereced by *d["server"]*, is *'mpilgrim'*

* **You can get values by key, but you can't get keys by value.**
  So *d["server"]* is *'mpilgrim'*, but *d["mpukgrim"]* raises an exception,
  because 'mpilgrim' is not a key.

3.1.2 Modifying a Dictionary
****************************

Example 3.2. Modifying a Dictionary

.. sourcecode:: ipython

   In [18]: d
   Out[18]: {'database': 'master', 'server': 'mpilgrim'}

   In [19]: d["database"] = "pubs"  # modify the value associated with key "database"

   In [20]: d
   Out[20]: {'database': 'pubs', 'server': 'mpilgrim'}

   In [21]: d["uid"] = "sa"  # add new key-value pairs

   In [22]: d
   Out[22]: {'database': 'pubs', 'server': 'mpilgrim', 'uid': 'sa'}

* You cannot have duplicate keys in a dictionary

* You can add new key-value pairs at any time. 
  This syntax is identical to modifying existing values.

Example 3.3. Dictionary Keys Are Case-Sensitive

.. sourcecode:: ipython

   In [27]: d = {}

   In [28]: d["key"] = "value"

   In [29]: d["key"] = "other value"

   In [30]: d
   Out[30]: {'key': 'other value'}

   In [31]: d["Key"] = "third value"

   In [32]: d
   Out[32]: {'Key': 'third value', 'key': 'other value'}
  
Example 3.4. Mixing Datatypes in a Dictionary

.. sourcecode:: ipython

   In [37]: d
   Out[37]: {'database': 'master', 'server': 'mpilgrim', 'uid': 'sa'}

   In [38]: d["retrycount"] = 3

   In [39]: d
   Out[39]: {'database': 'master', 'retrycount': 3, 'server': 'mpilgrim', 'uid': 'sa'}

   In [40]: d[42] = "douglas"

   In [41]: d
   Out[41]: {42: 'douglas',
             'database': 'master',
             'retrycount': 3,
             'server': 'mpilgrim',
             'uid': 'sa'}

3.1.3 Deleting Items From Dictionaries
**************************************

key funcs: 

.. sourcecode:: python
   
   del, clear()

Example 3.5. Deleting Items from a Dictionary

.. sourcecode:: ipython

   In [44]: d
   Out[44]: {42: 'douglas',
             'database': 'master',
             'retrycount': 3,
             'server': 'mpilgrim',
             'uid': 'sa'}

   In [45]: del d[42]

   In [46]: d
   Out[46]: {'database': 'master', 'retrycount': 3, 'server': 'mpilgrim', 'uid': 'sa'}

   In [47]: d.clear()

   In [48]: d
   Out[48]: {}

.. sourcecode:: python
   
   # lets you delete individual items from a dictionary by key.
   del d.[key]

   # deletes all items from a dictionary.
   d.clear()

3.1.4 Accessing Items in Dictionaries
*************************************

key funcs::
    
    dict.keys(), dict.values(), dict.items()

Example SP. The *Keys,values*, and *items* Functions

.. sourcecode:: ipython

   In [6]: params = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}

   In [7]: params.keys()
   Out[7]: ['pwd', 'database', 'uid', 'server']

   In [8]: params.values()
   Out[8]: ['secret', 'master', 'sa', 'mpilgrim']

   In [9]: params.items()
   Out[9]: [('pwd', 'secret'),
            ('database', 'master'),
            ('uid', 'sa'),
            ('server', 'mpilgrim')]

::

    # The keys method of a dictionary returns a list of all the keys.
    # The list is not in the ordr in which the dictionary was defined.
    dict.keys()

    # The values method returns a list of all the values.
    # The list is in the same order as the list returned by keys
    # params.values()[n] = params[params.keys()[n]]
    dict.values()

    # The items method returns a list of tuples of the form (key, value).
    dict.items()
   
.. _lists:

3.2. Lists
----------

A list in Python can hold arbitrary objects and can expand dynamically as new items
are added. (i.e., like *ArrayList* in Java)

* A list is an ordered set of elements
* lists are zero-based
* list elements do not need to be unique

3.2.1 Defining Lists
********************

Example 3.6. Defining a List

.. sourcecode:: ipython

   In [1]: li = ["a","b","mpilgrim","z","example"]  # create a list

   In [2]: li
   Out[2]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [3]: li[0]
   Out[3]: 'a'

   In [4]: li[4]
   Out[4]: 'example'
   
Example 3.7. Negative List Indices

.. sourcecode:: ipython

   In [5]: li
   Out[5]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [6]: li[-1]
   Out[6]: 'example'

   In [7]: li[-3]
   Out[7]: 'mpilgrim'
   
* A negative index accesses elements from the end of the list counting backwards.
  The last element of any non-empty list is always li[-1]

* If the negative index is confusing to you, think of it this way:
  li[-n] = li[len(li) - n]. (i.e., li[-3] == li[5-3] == li[2])

Example 3.8. Slicing a List

.. sourcecode:: ipython
   
   In [11]: li
   Out[11]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [12]: li[1:3]
   Out[12]: ['b', 'mpilgrim']

   In [13]: li[1:-1]
   Out[13]: ['b', 'mpilgrim', 'z']

   In [14]: li[0:3]
   Out[14]: ['a', 'b', 'mpilgrim'] 
   
* slice : a subset of list.
  (note: the return value is a new list containing all the elements of the list,
  in order, starting with the first slice index, up to but not including the 
  second slice index)

* Slicing works if one or both of the slice indices is negative.

Example 3.9. Slicing Shorthand

.. sourcecode:: ipython

   In [15]: li
   Out[15]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [16]: li[:3]
   Out[16]: ['a', 'b', 'mpilgrim']

   In [17]: li[3:]
   Out[17]: ['z', 'example']

   In [18]: li[:]
   Out[18]: ['a', 'b', 'mpilgrim', 'z', 'example']

* If left slice index is 0, you can leave it out.

* If right slice index is len(li), you can leave it out.

* If both slice indices are left out, all elements of the list are included.

.. tip::
   
   *li[:]* is not the same as the original *li* list; it is a new list that happens
   to have all the same elements.

   In other words, **li[:] is shorthand for making a complete copy of a list**

3.2.2 Adding Elements to Lists
******************************

key funcs

.. sourcecode:: python

   list.append(), list.insert(), list.extend()
   
Example 3.10 Adding Elements to a List

.. sourcecode:: ipython

   n [19]: li
   Out[19]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [20]: li.append("new")

   In [21]: li
   Out[21]: ['a', 'b', 'mpilgrim', 'z', 'example', 'new']

   In [22]: li.insert(2,"new")

   In [23]: li
   Out[23]: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']

   In [24]: li.extend(["two","elements"])

   In [25]: li
   Out[25]: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

.. sourcecode:: python
   
   # adds a single element to the end of the list
   list.append(element)

   # inserts a single element into a list
   # the numeric argument is the index of the first element that gets bumped out of pos.
   list.insert(element)

   # concatenates lists
   # there is only one argument, which is a list
   list.extends([list])

3.2.3 Searching Lists
*********************

key funcs

.. sourcecode:: python
  
   in, list.index(element)

Example 3.12 Searching a List

.. sourcecode:: ipython

   In [26]: li
   Out[26]: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

   In [28]: li.index("example")
   Out[28]: 5

   In [29]: li.index("new")
   Out[29]: 2

   In [30]: li.index("c")
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-30-f211222a0d52> in <module>()
   ----> 1 li.index("c")

   ValueError: 'c' is not in list

   In [31]: "c" in li
   Out[31]: False
 
.. sourcecode:: python

   # finds the first occurence of a value in the list and return the index.
   list.index(element)

   # to test whether a value is in the list.
   # returns True if the value is found or False if it is not.
   element in list

.. note::
   
   Python accepted almost anything in a boolean context (i.e., if statement), according to the following rules:

   * 0 is false; all other numbers are ture.
   * An empty string ("") is false; all other strings are true.
   * An empty list ([]) is false; all other lists are true.
   * An empty tuple (()) is false; all other tuples are true.
   * An empty dictionary ({}) is false; all other dictionaries are true.

3.2.4 Deleting List Elements
****************************

key funcs::
    
    list.remove(element), list.pop()

Example 3.13 Removing Elements from a List

.. sourcecode:: ipython

   In [32]: li
   Out[32]: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

   In [33]: li.remove("z")

   In [34]: li
   Out[34]: ['a', 'b', 'new', 'mpilgrim', 'example', 'new', 'two', 'elements']

   In [35]: li.remove("new")

   In [36]: li
   Out[36]: ['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']

   In [37]: li.remove("c")
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-37-f8d6d2097f1e> in <module>()
   ----> 1 li.remove("c")

   ValueError: list.remove(x): x not in list

   In [38]: li.pop()
   Out[38]: 'elements'

   In [39]: li
   Out[39]: ['a', 'b', 'mpilgrim', 'example', 'new', 'two']

::

    # removes the first occurence of a value from a list
    list.remove(element)

    # removes the last element of the list, and it returns the value that it removed.
    list.pop()

3.2.5 Counting in List
**********************

Key func::
    
    List.count(element)

Example SP. Count the number of appearance of a element

.. sourcecode:: ipython

   In [8]: li = ["a","mpilgrim","foo","b","c","b","d","d"]

   In [9]: li.count('b')
   Out[9]: 2

   In [10]: li.count('a')
   Out[10]: 1

::
    
    # returns the number of times a value occurs in a list.
    list.count(element)

3.2.6 Using List Operators
**************************

Example 3.14 List Operators

.. sourcecode:: ipython
    
   In [44]: li = ['a','b','mpilgrim']

   In [45]: li =  li + ['example','new']

   In [46]: li
   Out[46]: ['a', 'b', 'mpilgrim', 'example', 'new']

   In [47]: li += ['two']

   In [49]: li
   Out[49]: ['a', 'b', 'mpilgrim', 'example', 'new', 'two']

   In [50]: li = [1,2]*3

   In [51]: li
   Out[51]: [1, 2, 1, 2, 1, 2] 

* Lists can also concatenated with the + operator. list = list + otherlist has the same result as
  list.extend(otherlist)

.. note::
   
   the + operator returns a new (concatenated) list as a value, whereas extend only alters an existing list.
   This means that *extend is faster, especially for large lists*.

* The \* operator works on lists as a repeater. li = [1,2] \* 3 is equivalent to li = [1,2] + [1,2] + [1,2]

.. _tuples:

3.3. Tuples
-----------

.. note:: 

   A tuple is an immutable list. A tuple cannot be changed in any way once it is created.
 
Example 3.15 Defining a tuple

.. sourcecode:: ipython

   In [1]: t = ("a","b","mpilgrim","z","example")

   In [2]: t
   Out[2]: ('a', 'b', 'mpilgrim', 'z', 'example')

   In [3]: t[0]
   Out[3]: 'a'

   In [4]: t[-1]
   Out[4]: 'example'

   In [5]: t[1:3]
   Out[5]: ('b', 'mpilgrim')
   
* A tuple is very similar to a list. 

Example 3.16 Tuples are immutable

.. sourcecode:: ipython

   In [6]: t
   Out[6]: ('a', 'b', 'mpilgrim', 'z', 'example')

   In [7]: t.append("new")
   ---------------------------------------------------------------------------
   AttributeError                            Traceback (most recent call last)
   <ipython-input-7-2752b0468aa7> in <module>()
   ----> 1 t.append("new")

   AttributeError: 'tuple' object has no attribute 'append'

   In [8]: t.remove("z")
   ---------------------------------------------------------------------------
   AttributeError                            Traceback (most recent call last)
   <ipython-input-8-ae25cf082d3e> in <module>()
   ----> 1 t.remove("z")

   AttributeError: 'tuple' object has no attribute 'remove'

   In [9]: t.index("example")
   Out[9]: 4

   In [10]: "z" in t
   Out[10]: True

* You cannot modify the tuples.

* You can find elements in a tuple.

* Also, you can use in to see if an element exists in the tuple.

.. admonition:: Usage of tuples

   * Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to with it
     is iterate through it, use a tuple instead of a list

   * It makes your code safer if you "write-protect" data that does not need to be changed.

   * Tuples can be used as keys in dictionary. (since keys in dictionary should be immutable)

   * Tuples are used in string formatting.

Example 3.17 Convert between tuple and list

.. sourcecode:: ipython

   In [24]: t
   Out[24]: ('a', 'b', 'mpilgrim', 'z', 'example')

   In [25]: list(t)
   Out[25]: ['a', 'b', 'mpilgrim', 'z', 'example']

   In [26]: tuple(t)
   Out[26]: ('a', 'b', 'mpilgrim', 'z', 'example')

::
  
    # convert tuple to list
    list(t)

    # convert list to tuple
    tuple(t)

.. _declare_var:

3.4. Declaring variables
------------------------

Example 3.17 Defining the myParams Variable

::
    
    if __name__ == "__main__":
        myParams = {"server":"mpilgrim", \
                    "database":"master",\
                    "uid":"sa",\
                    "pwd":"secret"\
        }

* a backslash ("\\") seving as a line-continuation marker.

* Actually, expressions in parentheses, straight brackets, or curly braces (like defining a dictionary) can be split
  into multiple lines with or without the line continuation character ("\\")
 
3.4.2 Assigning Multiple Values at Once
***************************************

Example 3.19 Assigning multiple values at once

.. sourcecode:: ipython

   In [6]: x,y,z = 'd','c','f'

   In [7]: x
   Out[7]: 'd'

   In [8]: y
   Out[8]: 'c'

   In [9]: z
   Out[9]: 'f'

Example 3.20 Assigning Consecutive Values

.. sourcecode:: ipython

   In [11]: range(7)
   Out[11]: [0, 1, 2, 3, 4, 5, 6]

   In [12]: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)

   In [13]: MONDAY
   Out[13]: 0

   In [14]: TUESDAY
   Out[14]: 1

.. _format_string:

3.5. Formatting Strings
-----------------------

Example 3.21 Introducing String Formatting

.. sourcecode:: ipython

   In [1]: k = "uid"

   In [2]: v = "sa"

   In [3]: "%s = %s" % (k,v)
   Out[3]: 'uid = sa' 

* [3]: the whole expression evaluates to a string. The first %s is replaced by the value of k; the second %s is 
  replaced by the value of v. All other characters in the string (in this case, the equal sign) stay as they are.

Example 3.22 String Formatting vs. Concatenating

.. sourcecode:: ipython

   In [4]: uid = "sa"

   In [5]: pwd = "secret"

   In [7]: print pwd + " is not a good password for " + uid
   secret is not a good password for sa

   In [8]: print "%s is not a good password for %s" % (pwd,uid)
   secret is not a good password for sa

   In [9]: userCount = 6

   In [10]: print "Users connected: %d" %(userCount, )
   Users connected: 6

   In [11]: print "Users connected: " + userCount
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-11-be2e27f72c6d> in <module>()
   ----> 1 print "Users connected: " + userCount

   TypeError: cannot concatenate 'str' and 'int' objects
  
* [7]: + is the string concatenation operator.

* [10]: (userCount, ) is a tuple with one element. The comma is required when defining a tuple with one element.
 
* [11]: string concatenation works only when everything is already a string.

Example 3.23 Formatting Numbers

.. sourcecode:: ipython

   In [13]: print "Today's stock price: %f" % 50.4625
   Today's stock price: 50.462500

   In [14]: print "Today's stock price: %.2f" % 50.4625
   Today's stock price: 50.46

   In [15]: print "Today's stock price: %+.2f" % 1.5
   Today's stock price: +1.50

* The %f string formmatting option treats the value as a decimal

* The ".2" modifier of the %f option truncates the value to two decimal places

.. _mapping_lists:

3.6. Mapping Lists
------------------

List comprehension in Python provides a compact way of mapping a list into another list by applying a function
to each of the elements of the list.

Example 3.24 Introducing List comprehensions

.. sourcecode:: ipython
    
   In [1]: li = [1,9,8,4]

   In [2]: [elem*2 for elem in li]
   Out[2]: [2, 18, 16, 8]

   In [3]: li
   Out[3]: [1, 9, 8, 4]

   In [4]: li = [elem*2 for elem in li]

   In [5]: li
   Out[5]: [2, 18, 16, 8]

* [2]: li is the list you're mapping. 
       Python loops through li one element at a time, temporarily assigning the value of each element to the elem.
       Python then applies the function elem \* 2 that appends that result to the returned list.

* [3]: list comprehensions do not change the original list.

Example 3.26 List Comprehensions in buildConnectionString, step by step

.. sourcecode:: ipython

   In [12]: params
   Out[12]: {'database': 'master', 'pwd': 'secret', 'server': 'mpilgrim', 'uid': 'sa'}

   In [13]: params.items()
   Out[13]: [('pwd', 'secret'),
             ('database', 'master'),
             ('uid', 'sa'),
             ('server', 'mpilgrim')]

   In [14]: [k for k,v in params.items()]
   Out[14]: ['pwd', 'database', 'uid', 'server']

   In [15]: [v for k,v in params.items()]
   Out[15]: ['secret', 'master', 'sa', 'mpilgrim']

   In [16]: ["%s=%s"%(k,v) for k,v in params.items()]
   Out[16]: ['pwd=secret', 'database=master', 'uid=sa', 'server=mpilgrim']
   
* Note that you're using two variables to iterate through the params.items() list. 
  This is another use of multi-variable assignment. The first element of params.items() is ('pwd','secret'),
  so in the first iteration of the list comprehension, k will get 'pwd' and v will get 'secret'.
  
.. _join and split:

3.7. Joining Lists and Splitting Strings
-----------------------------------------

key funcs

::
    
    delim.join(list), string.split(delim)


Example 3.27 Output of odbchelper.py

.. sourcecode:: ipython

   In [17]: params
   Out[17]: {'database': 'master', 'pwd': 'secret', 'server': 'mpilgrim', 'uid': 'sa'}

   In [18]: ["%s=%s"%(k,v) for k,v in params.items()]
   Out[18]: ['pwd=secret', 'database=master', 'uid=sa', 'server=mpilgrim']

   In [20]: ";".join(["%s=%s"%(k,v) for k,v in params.items()])
   Out[20]: 'pwd=secret;database=master;uid=sa;server=mpilgrim'
  
::
    
    # to join any list of strings into a single string, use the john method of a string object
    # join works only on lists of strings
    delim.join(list)

* In this case, the join method joins the elements of the list into a single string, with each element
  separated by a semi-colon. 

* The delimiter doesn't need to be a semi-colon; It can be any string.

Example 3.28 Splitting a String

.. sourcecode:: ipython

   In [23]: li = ['server=mpilgrim','uid=sa','database=master','pwd=secrect']

   In [24]: s = ";".join(li)

   In [25]: s
   Out[25]: 'server=mpilgrim;uid=sa;database=master;pwd=secrect'

   In [26]: s.split(';')
   Out[26]: ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secrect']

   In [27]: s.split(';',1)
   Out[27]: ['server=mpilgrim', 'uid=sa;database=master;pwd=secrect']
   
::
    
    # split reverses join by splitting a string into a multi-element list.
    # note that the delimiter (";") is stripped out completely; it does not appear in any of the elements of the returned list.
    string.split(delim)

* split takes an optional 2nd argument, which is the number of times to split.

.. tip::

   anystring.split(delimiter,1) is a useful technique when you want to search a string for a substring and then work with everything
   before the substring (which ends up in the first element of the returned list) and
   everything after it (which ends ip in the second element).
