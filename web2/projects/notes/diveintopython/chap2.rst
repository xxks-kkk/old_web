.. _chap2.rst:

====================
First Python Program
====================

.. _diving in:

2.1 Diving in
--------------
Example 2.1. odbchelper.py

.. sourcecode:: python

    def buildConnectionString(params):
        """Build a connection string from a dictionary of parameters.

        Returns string.
        """
        return ";".join(["%s=%s" % (k,v) for k,v in params.items()])
    
    if __name__ = "__main__":
        myParams = {"server":"mpilgrim",\
                    "database":"master",\
                    "uid":"sa",\
                    "pwd":"secret"
        }
        print buildConnectionString(myParams)

Output:

.. sourcecode:: python

    server=mpilgrim;uid=sa;database=master;pwd=secret


.. _Documenting Functions:

2.2 Documenting Functions
--------------------------

* You can document a Python function by giving it a doc string.

* Triple quotes  *"""* used when defining a doc string.

    - Triple quotes are useful to define a string with both single and double quotes.
    - Doc string, if it exists, must be the first thing defined in a function (that is, the first
      thing after the colon).

.. _Everything is an object:

2.3 Everything is an object
----------------------------

Example 2.3. Accessing the buildConnectionString Function's **doc** string

.. sourcecode:: ipython

   In [1]: import odbhelper

   In [2]: params = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}

   In [3]: print odbhelper.buildConnectionString(params)
   Out[3]: server=mpilgrrim;uid=sa;database=master;pwd=secret

   In [4]: print odbhelper.buildConnectionString.__doc__
   Out[4]: Build a connection string from a dictionary

           Returns string.

*  when you want to use functions defined in imported modules, you need to include the module name.

.. _Import Search Path:

2.4 The import Search Path
--------------------------

Example 2.4. Import Search Path

.. sourcecode:: ipython
   
   In [1]: import sys

   In [2]: sys.path
   Out[2]: ['',
    '/usr/local/lib/python2.7/dist-packages/pymc-2.2-py2.7-linux-i686.egg',
    '/usr/local/lib/python2.7/dist-packages/Jinja2-2.6-py2.7.egg',
    '/usr/lib/python2.7',
    '/usr/lib/python2.7/plat-linux2',
    '/usr/lib/python2.7/lib-tk',
    '/usr/lib/python2.7/lib-old',
    '/usr/lib/python2.7/lib-dynload',
    '/usr/local/lib/python2.7/dist-packages',
    '/usr/local/lib/python2.7/dist-packages/PIL',
    '/usr/lib/python2.7/dist-packages',
    '/usr/lib/python2.7/dist-packages/PIL',
    '/usr/lib/python2.7/dist-packages/gst-0.10',
    '/usr/lib/python2.7/dist-packages/gtk-2.0',
    '/usr/lib/pymodules/python2.7',
    '/usr/lib/python2.7/dist-packages/ubuntu-sso-client',
    '/usr/lib/python2.7/dist-packages/ubuntuone-client',
    '/usr/lib/python2.7/dist-packages/ubuntuone-control-panel',
    '/usr/lib/python2.7/dist-packages/ubuntuone-couch',
    '/usr/lib/python2.7/dist-packages/ubuntuone-storage-protocol',
    '/usr/lib/python2.7/dist-packages/wx-2.8-gtk2-unicode',
    '/usr/lib/python2.7/dist-packages/IPython/extensions']

   In [3]: sys
   Out[3]: <module 'sys' (built-in)>
   In [4]: sys.path.append(os.path.abspath('sphinxext'))

* sys.path is a list of directory names that constitute the current search path.
  Python will look through these directories (in this order) for a .py file matching the module name you're trying
  to import.

* You can add a new directory to Python's search path at runtime by appending the directory name to sys.path,
  and then Python will look in that directory as well, whenever you try to import a module.
  (i.e., here I try to add the sphinx extension directory to the search path)

* *everything in Python is an object*. Strings are objects. Lists are objects. Functions are objects. Even modules
  are objects.

.. _Indenting Code:

2.5 Indenting Code
------------------

Example 2.5. Indenting the **fib** Function

.. sourcecode:: python

   def fib(n):
       # you can mix and match to print several thing on one line
       # by using a comma-separated list of values.
       # Each value is printed on the same line, separated by spaces (i.e., "n = 5")
       print 'n = ', n
       if n > 1:
            return n * fib(n-1)
       else:
            print 'end of the line'
            return 1

.. _Testing Modules:

2.6 Testing Modules
-------------------

Python modules are objects and have several useful attributes. You can use this to easily
test your modules as you write them.

.. sourcecode:: python

   if __name__ = "__main__":

* parentheses are not required around the **if** expression

* all modules have a built-in attribute *__name__*,
  A module's *__name__* depends on how you're using the module.
    
    - If you *import* the module, then *__name__* is the module's filename, whithout a directory path or file extension
    - You can also run the module directly as a standalone program, 
      in which case *__name__* will be a special default value, *__main__*

.. sourcecode:: ipython
   
   In [1]: import odbhelper
   In [2]: odbhelper.__name__
   Out[2]: 'odbhelper'

* knowning this, you can design a test suite for your module within the module itself by putting it in this **if** 
  statement. When you run the module directly, *__name__* is *__main__*, so the test suite executes. When you import
  the module, *__name__* is something else, so the test suite is ignored. This makes it easier to develop and debug new
  modules before integrating them into a larger program.
