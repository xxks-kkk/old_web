.. _chap5.rst:

==============================
Objects and Object-Orientation
==============================

Object-oriented Python programming:

* you can define your own classes

* inherit from your own or built-in classes

* instantiate the classes you've defined

.. _divingin:

5.1. Diving In
--------------

Example 5.1 fileinfo.py (download `here <../../../_static/projects/notes/diveintopython/py/fileinfo.py>`_)

.. sourcecode:: python

   """Framework for getting filetype-specific metadata.

   Instantiate appropriate class with filename.  Returned object acts like a
   dictionary, with key-value pairs for each piece of metadata.
       import fileinfo
       info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
       print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

   Or use listDirectory function to get info on all files in a directory.
       for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
           ...

   Framework can be extended by adding classes for particular file types, e.g.
   HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Each class is completely responsible for
   parsing its files appropriately; see MP3FileInfo for example.

   """

   import os
   import sys
   from UserDict import UserDict

   def stripnulls(data):
       "strip whitespace and nulls"
       return data.replace("\00", " ").strip()

   class FileInfo(UserDict):
       "store file metadata"
       def __init__(self, filename=None):
           UserDict.__init__(self)
           self["name"] = filename
    
   class MP3FileInfo(FileInfo):
       "store ID3v1.0 MP3 tags"
       tagDataMap = {"title"   : (  3,  33, stripnulls),
                     "artist"  : ( 33,  63, stripnulls),
                     "album"   : ( 63,  93, stripnulls),
                     "year"    : ( 93,  97, stripnulls),
                     "comment" : ( 97, 126, stripnulls),
                     "genre"   : (127, 128, ord)}
    
       def __parse(self, filename):
           "parse ID3v1.0 tags from MP3 file"
           self.clear()
           try:
               fsock = open(filename, "rb", 0)
               try:
                   fsock.seek(-128, 2)
                   tagdata = fsock.read(128)
               finally:
                   fsock.close()
               if tagdata[:3] == 'TAG':
                   for tag, (start, end, parseFunc) in self.tagDataMap.items():
                       self[tag] = parseFunc(tagdata[start:end])
           except IOError:
               pass

       def __setitem__(self, key, item):
           if key == "name" and item:
               self.__parse(item)
           FileInfo.__setitem__(self, key, item)

   def listDirectory(directory, fileExtList):
       "get list of file info objects for files of particular extensions"
       fileList = [os.path.normcase(f) for f in os.listdir(directory)]
       fileList = [os.path.join(directory, f) for f in fileList \
                   if os.path.splitext(f)[1] in fileExtList]
       def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
           "get file info class from filename extension"
           subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
           return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
       return [getFileInfoClass(f)(f) for f in fileList]

   if __name__ == "__main__":
       
       # This program's output depends on the files on your hard drive
       # To get meaningful output, you'll need to change the directory path to 
       # point to a directory of MP3 files on your own machine.
       for info in listDirectory("/music/_singles/", [".mp3"]):
           print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
           print 

Sample Output:

::
    
    name=/music/_singles/009 Sound System - With A Spirit.mp3

    album=Lean On Me: The Best of Bill W
    comment=
    name==/music/_singles/01 Bill Withers - Ain't No Sunshine.mp3
    title=Ain't No Sunshine
    artist=Bill Withers
    year=1980
    genre=255

    album=Sampler 001
    comment=
    name=/music/_singles/02 I'm Yours.mp3
    title=I'm Yours
    artist=Jason Mraz
    year=2005
    genre=17

    album=State of Grace - Single
    comment=
    name=/music/_singles/Taylor Swift - State of Grace.mp3
    title=State of Grace
    artist=Taylor Swift
    year=2012
    genre=2

.. _import_modules:

5.2. Importing Modules Using *from module import*
-------------------------------------------------

.. admonition:: basic *from module import* syntax

   ::

        # import UserDict from UserDict module
        from UserDict import UserDict
        
        # from UserDict module import everything
        from UserDict import *

* difference with *import module* syntax:
  the attributes and methods of the imported module types are imported directly into
  the local namespace, so they are available directly, without qualification by 
  module name.
 
Example 5.2 import module *vs* from module import

.. sourcecode:: ipython

   In [14]: import types

   In [16]: types.FunctionType
   Out[16]: function

   In [17]: FunctionType
   ---------------------------------------------------------------------------
   NameError                                 Traceback (most recent call last)
   <ipython-input-17-66c15b651254> in <module>()
   ----> 1 FunctionType

   NameError: name 'FunctionType' is not defined

   In [18]: from types import FunctionType

   In [20]: FunctionType
   Out[20]: function

[16]: 
    Note that the attribute, ``FunctionType``, must be qualified by the module name, ``types``.

[17]: 
    ``FunctionType`` by itself has not been defined in this namespace; 
    it exists only in the context of ``types``.

[18]: 
    This syntax imports the attribute ``FunctionType`` from the ``types`` module 
    directly into the local namespace.

[20]: 
    Now FunctionType can be accessed directly, without reference to ``types``.

.. admonition:: when to use *from module import*?

   * If you will be accessing attributes and methods often and don't want to type the module name over and      over, use *from module import*

   * If you want to selectively import some attributes and methods but not others, use *from module import*

   * If the module contains attributes or functions with the same name as ones in your module, you must
     use *import module* to avoid name conflicts.

.. _define_class:

5.3. Defining Classes
---------------------

.. admonition:: define class

   .. sourcecode:: python

      # if there is no inheritance, then the base class (include parentheses) should be omitted.
      class Classname (base class):
          code

Example 5.3 The Simplest Python Class (**without inheritance**)

::

    # the class, Loaf, doesn't inherit from any other class
    # class names are capitalized
    class Loaf:
        # placeholder: doesn't do anything
        pass

Example 5.4 Defining the Fileinfo Class (**with inheritance**)

.. sourcecode:: python
    
   # UserDict is a class that acts like a dictionary, 
   # allowing you to essentially subclass the dictionary datatype and add your own behavior
   # There are similar classes UserList and UserString
   from UserDict import UserDict
    
   # FileInfo class is inherited from the UserDict class( which was imported from the UserDict module)
   class FileInfo(UserDict):

* In Python, the ancestor of a class is simply listed in parentheses immediately after the class name. 
  There is no special keyword like ``extends`` in Java.

* Python supports multiple inheritance. In the parentheses following the class name, you can list as many 
  ancestor classes as you like, separated by commas.

5.3.1 Initializing and Coding Classes
*************************************

Example 5.5 Initializing the FileInfo Class

.. sourcecode:: python

   class FileInfo(UserDict):
       "store file metadata"

       # __init__ is called immediately after an instance of the class is created
       def __init__(self, filename=None):

.. admonition:: is __init__ the constructor of the class?

   It would be tempting but incorrect to call this the constructor of the class:

   * tempting:
   
        - looks like a constructor (by convention, ``__init__`` is the first method dfined for the class)
        - acts like one (it's the first piece of code executed in a newly created instance of the class)
        - sounds like one ("init" certainly suggest a constructor-ish nature)

   * incorrect:

        - the object has already been constructed by the time ``__init__`` is called, 
          and you already have a valid reference to the new instance of the class.

   But ``__init__`` is the closes thing you're going to get to a constructor in Python, 
   and it fills much the same role.

.. admonition:: self in argument list

   The first argument of every class method, including ``__init__``, is always a reference to the current 
   instance of the class.

   By convention, this argument is always named ``self``.

   In the ``__init__`` method, ``self`` referes to the newly created object;
   in other class methods, it refers to the instance whose method was called.

   You need to specify ``self`` explicitly when defining the method,
   you do not specify it when calling the method; Python will add it for you automatically.

* ``self`` in Python fills the role of the reserved word ``this`` in Java.

Example 5.6 Coding the FileInfo class

.. sourcecode:: python

   class FileInfo(UserDict):
       "store file metadata"
       def __init__ (self, filename=None):
           # _init_ methods are optional, but when you define one, 
           # you must remember to explicitly call the ancestor's __init__ method (if it defines one)
           UserDict.__init__(self)
           self["name"] = filename

* In general, whenever a descendant wants to extend the behavior of the ancestor, the descendant method
  must explicitly call the ancestor method at the proper time, with the proper arguments.

5.3.2 Knowing When to Use *self* and *__init__*
***********************************************

* When defining your class methods, you *must* explicitly list self as the first argument for each method,
  including ``__init__``.

* When you call a method of an ancestor class from within your class, you *must* include ``self`` argument.

* When you call your class method from outside, you do not specify anything for the ``self`` argument; 
  skip it entirely, and Python automatically adds the instance reference for you.


.. _instantiate_class:

5.4. Instantiating Classes
--------------------------

.. admonition:: instantiate class

   To instantiate a class, simply call the class as if it were a function, 
   passing the arguments that the ``__init__`` method defines. 
   The return value will be the newly created object.

Example 5.7 Creating a FileInfo Instance

.. sourcecode:: ipython

   In [15]: import fileinfo

   In [17]: f = fileinfo.FileInfo("/home/zeyuan_hu/Music/taylor.mp3")

   In [18]: f.__class__
   Out[18]: fileinfo.FileInfo

   In [19]: f.__doc__
   Out[19]: 'store file metadata'

   In [20]: f
   Out[20]: {'name': '/home/zeyuan_hu/Music/taylor.mp3'}

[17]: 
      You are creating an instance of the ``FileInfo`` class (defined in the ``fileinfo`` module) and 
      assigning the newly created instance to the variable ``f``.

[17]: 
      You are passing one argument, ``/home/zeyuan_hu/Music/taylor.mp3``, which will end up as the 
      ``filename`` argument in ``Fileinfo``'s ``__init__`` method.

[18]: 
      Every class instance has a built-in attribute, ``__class__``, which is the object's class


.. _explore_UserDict:

5.5. Exploring UserDict: A Wrapper Class
----------------------------------------

As you've seen, ``FileInfo`` is a class that acts like a dictionary. To explore this further, let's look at
the ``UserDict`` class in the ``UserDict`` module, which is the ancestor of the ``FileInfo`` class.

Example 5.9 Defining the UserDict Class

.. sourcecode:: python
   :linenos:

   # UserDict is a base class, not inherited from any other class
   class UserDict:
       def __init__(self, dict=None):
           self.data = {}
           if dict is not None: self.update(dict)

[3]:
    This is the ``__init__`` method that you overrode in the ``FileInfo`` class.
    Note that the argument list in this ancestor class is different than the descendant.
    That's OK; each subclass can have its own set of arguments, as long as it calls the ancestor with 
    the correct arguments. Here the ancestor class has a way to define initial values (by passing a
    dictionary in the ``dict`` argument) which the ``FileInfo`` does not use.

[4]:
    .. admonition:: data attributes (instance variables)
    
       * Python supports data attributes (called "instance variables" in Java).
       * Data attributes are pieces of data held by a specific instance of a class. 
       * In this case, each instance of ``UserDict`` will have a data attribute ``data``.
       * To reference a data attribute:
        
            - from code outside the class, you qualify it with the instance name, ``instance.data``, in
              the same way that you qualify a function with its module name.

            - from within the class, you use ``self`` as the qualifier.

       * By convention, all data attributes are initialized to reasonable values in the ``__init__`` 
         method.
     
    
    .. tip::
        
       Always assign an initial value to all of an instance's data attributes in the ``__init__`` method.
       It will save you hours of debugging later, tracking down ``AttributeError`` exceptions because
       you're referencing uninitialized (and therefore non-existent) attributes.

[5]:
    The ``update`` method is a dictionary duplicator: 
       
    * it copies all the keys and values from one dictionary to another.

    * this does *not* clear the target dictionary first; if the target dictionary already has some keys,
      the ones from the source dictionary will be overwritten, but others will be left untouched.

    Think of ``update`` as a merge function, not a copy function.

[5]:
    a shortcut syntax you can use when you have only one statement in a block.

.. warning::

   Unlike Java, Python does *not* support **function overloading by argument list** 
   (*i.e.* one class have multiple methods with the same name but a different number of arguments, 
   or arguments of different types.): it has no form of function overloadng whatsoever. 
   Method are defined solely by their name, and there can be only one method per class with a given name.

   So, if a descendant class has an ``__init__`` method, it *always* overrides the ancestor ``__init__``
   method, even if the descendant defines it with a different argument list. And the same rule applies to
   any other method.

Example 5.10 ``UserDict`` Normal Methods (wrapper class methods)

.. sourcecode:: python
   :linenos:

   def clear(self): self.data.clear()
                    
   def copy(self):
       if self.__class__ is UserDict:
            return UserDict(self.data)
       import copy
       return copy.copy(self)

   def keys(self): return self.data.keys()

   def items(self): return self.data.items()

   def values(self): return self.data.values()

[1]:
   ``clear`` is a normal class method; it is publicly available to be called by anyone at any time.
   Notice that ``clear``, like all class methods, has ``self`` as its first argument.

[1]:
    tha basic technique of this wrapper class:
        
        store a real dictionary (``data``) as a data attribute, define all the methods that a real
        dictionary has, and have each class method redirect to the corresponding method on the real
        dictionary.
 
[3]:
    the ``copy`` method of a real dictionary returns a new dictionary that is an exact duplicate of the 
    original (all the same key-value pairs). But ``UserDict`` can't simply redirect to ``self.data.copy``,
    because that method returns a real dictionary, and what you want is to return a new instance that is
    the same class as ``self``

[3]:
    You use the ``__class__`` attribute to see if ``self`` is a ``UserDict``:

        - if so, you're golden, because you know how to copy a ``UserDict``:
          
            just create a new ``UserDict`` and give it the real dictionary that you've squirreled away
            in ``self.data``. Then you immediately return the new ``UserDict``.

        - if ``self.__class__`` is not ``UserDict``, then ``self`` must be some subclass of ``UserDict``
          (like maybe ``FileInfo``). ``UserDict`` doesn't know how to make an exact copy of one of its
          descendants; there could, for instance, be other data attributes defined in the subclass, so 
          you would need to iterate through them and make sure to copy all of them:

            Luckily, Python comes with a module to do exactly this, and it's called ``copy``. ``copy`` can
            copy arbitrary Python objects, and that's how you're using it here.

.. admonition:: about UserDict

   In versions of Python prior to 2.2, you could not directly subclass built-in datatypes like strings,
   lists, and dictionaries. To compensate for this, Python comes with wrapper classes that mimic the 
   behavior of these built-in datatypes: ``UserString``, ``UserList``, ``UserDict``.

   In Python 2.2 and later, you can inherit classes directly from built-in datatypes like ``dict``.

   This can be seen in ``fileinfo_fromdict.py`` 
   (download `here <../../../_static/projects/notes/diveintopython/py/fileinfo_fromdict.py>`_)

Example 5.11 Inheriting Directly from Built-In Datatype dict

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 1

   class FileInfo(dict):
       "store file metadata"
       def __init__(self, filename=None):
           self["name"] = filename

Example 5.6 Inheriting from UserDict class

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 1, 4

   class FileInfo(UserDict):
       "store file metadata"
       def __init__ (self, filename=None):
           UserDict.__init__(self)
           self["name"] = filename

difference with ``UserDict`` version:
    
    - You don't need to import the ``UserDict`` module, since ``dict`` is a built-in datatype and
      is always available.

    - You are inheriting from ``dict`` directly, instead of from ``UserDict.UserDict``.

    - Because of the way ``UserDict`` works internally, it requires you to manually call its ``__init__``
      method to properly initialize its internal data structures. 

      ``dict`` does not work like this; it is not a wrapper, and it requires no explicitly initialization.

.. _special_class_method:

5.6. Special Class Methods
--------------------------

In addition to normal class methods, there are a number of special methods that Python classes can define.

Instead of being called directly by your code (like normal methods), special methods are called for you by
Python in particular cirmustances or when specific syntax is used.

*key idea* of special class methods: 
    provide a way to map non-method-calling syntax into method calls

5.6.1 Getting and Setting Items
*******************************

Example 5.12 The ``__grtitem__`` Special Method

.. sourcecode:: python

   def __getitem__(self,key): return self.data[key]

.. sourcecode:: ipython

   In [38]: f = fileinfo.FileInfo("./Taylor Swift - State of Grace.mp3")

   In [39]: f
   Out[39]: {'name': './Taylor Swift - State of Grace.mp3'}

   In [40]: f.__getitem__("name")
   Out[40]: './Taylor Swift - State of Grace.mp3'

   In [41]: f["name"]
   Out[41]: './Taylor Swift - State of Grace.mp3'

[40]:
    Well, you can call __getitem__ directly, but in practice you wouldn't actually do that; I'm just doing
    it here to show you how it works. The right way to use ``__getitem__`` is to get Python to call it for
    you.

[41]:
    This looks just like syntax you would use to get a dictionary value, and in fact it returns the value
    you would expect. But here's the missing link: under the covers, Python has converted this syntax to 
    the method call ``f.__getitem__("name")``. That's why ``__getitem__`` is a special class method; not
    only can you call it yourself, you can get Python to call it for you by using the right syntax.

Example 5.13 The ``__setitem__`` Special Method

.. sourcecode:: python

   def __setitem__(self, key, item): self.data[key] = item

.. sourcecode:: ipython

   In [42]: f = fileinfo.FileInfo("./Taylor Swift - State of Grace.mp3")

   In [43]: f.__setitem__("genre",31)

   In [44]: f
   Out[44]: {'genre': 31, 'name': './Taylor Swift - State of Grace.mp3'}

   In [45]: f["genre"] = 32

   In [46]: f
   Out[46]: {'genre': 32, 'name': './Taylor Swift - State of Grace.mp3'}

``__setitem__`` is a special class method because it gets called for you, but it's still a class method.
Just as easily as the ``__setitem__`` method was defined in ``UserDict``, you can redefine it in the 
descendant class to override the ancestor method. This allows you to define classes that act like
dictionaries in some ways but define their own behavior above and beyong the built-in dictionary.

Example 5.14 Overriding ``__setitem__`` in ``MP3FileInfo``

.. sourcecode:: python
   :linenos:

   def __setitem__(self, key, item):
       if key == "name" and item:
            self.__parse(item)
       FileInfo.__setitem__(self, key, item)

[1]:
    Notice that this ``__setitem__`` method is defined exactly the same way as the ancestor method.
    (override)

[3]:
    This is another class method defined in ``MP3FileInfo``, and when you call it, you qualify it with
    ``self``. Just calling ``__parse`` would look for a normal function defined outside the class, which
    is not what you want. Calling ``self.__parse`` will look for a class method defined within the class.

[4]:
    After doing this extra processing, you want to call the ancestor method. Remember that this is never
    done for you in Python; you must do it manually. Note that you're calling the immediate ancestor,
    ``FileInfo``, wven though it doesn't have a ``__setitem__`` methd. That's okay, because Python will
    walk up the ancestor tree until it finds a class with the method you're calling, so this line of code
    will eventually find and call the ``__setitem__`` defined in ``UserDict``.

.. note::

   When accessing data attribute within a class, you need to qualify the attribute name:
   ``self.attribute``. When calling other methods within a class, you need to qualify the method name:
   ``self.method``.

Example 5.15 Setting an ``MP3FileInfo``'s name

.. sourcecode:: ipython

   In [48]: import fileinfo

   In [49]: mp3file = fileinfo.MP3FileInfo()

   In [50]: mp3file
   Out[50]: {'name': None}

   In [51]: mp3file["name"] = "./Taylor Swift - State of Grace.mp3"

   In [52]: mp3file
   Out[52]: {'album': 'State of Grace - Single', 'comment': '', 
             'name': './Taylor Swift - State of Grace.mp3', 'title': 'State of Grace', 
             'artist': 'Taylor Swift', 'year': '2012', 'genre': 2} 

[49]:
    First you create an instance of ``MP3FileInfo``, without passing it a filename. Since ``MP3FileInfo``
    has no ``__init__`` method of its own, Python walks up the ancestor tree and finds the ``__init__``
    method of ``FileInfo``. This ``__init__`` method manually calls the ``__init__`` method of 
    ``UserDict`` and then sets the ``name`` key to ``filename``, which is ``None``, since you didn't pass
    a filename. Thus, ``mp3file`` initially looks like a dictionary with one key, ``name``, whose value is
    ``None``.

.. _advanced_special_class_methods:

5.7. Advanced Special Class Methods
-----------------------------------

Python has more special methods than just ``__getitem__`` and ``__setitem__``.

This example shows some of the other special methods in ``UserDict``.

Example 5.16 More Special Methods in ``UserDict``

.. sourcecode:: python
    
   # __repr__ is called when you call repr(instance)
   # repr function is a built-in function that returns a string representation of an object
   def __repr__(self): return repr(self.data)
   
   # __cmp__ is called when you compare class instances by using "=="
   def __cmp__(self, dict):
       if isinstance(dict, UserDict):
           return cmp(self.data, dict.data)
       else:
           return cmp(self.data, dict)

   # __len__ is called when you call len(instance)
   # len function is a built-in function that returns the length of an object
   def __len__(self): return len(self.data)
    
   # __delitem__ is called when you call del instance[key]
   def __delitem__(self, key): del self.data[key]

.. note::
    
   the difference between Java and Python in terms of string comparison

        +----------------------+-------------------+--------------+
        |                      |       Java        | Python       |
        +======================+===================+==============+
        | object identity *    |    str1 == str2   | str1 is str2 |
        +----------------------+-------------------+--------------+
        | cmp string values    | str1.equals(str2) | str1 == str2 |
        +----------------------+-------------------+--------------+

   \*: determine whether two string variables reference the same physcial memory location

.. _class_attribute:

5.8. Introducing Class Attributes
---------------------------------

data attributes: variables owned by a specific instance of a class.

class attributes: variables owned by the class itself.

Example 5.17 Introducing Class Attributes

.. sourcecode:: python

   class MP3FileInfo(FileInfo):
       "store ID3v1.0 MP3 tags"
       tagDataMap = {"title"   : (  3,  33, stripnulls),
                     "artist"  : ( 33,  63, stripnulls),
                     "album"   : ( 63,  93, stripnulls),
                     "year"    : ( 93,  97, stripnulls),
                     "comment" : ( 97, 126, stripnulls),
                     "genre"   : (127, 128, ord)}

.. sourcecode:: ipython

   In [53]: import fileinfo

   In [54]: fileinfo.MP3FileInfo
   Out[54]: fileinfo.MP3FileInfo

   In [55]: fileinfo.MP3FileInfo.tagDataMap
   Out[55]: {'album': (63, 93, <function fileinfo.stripnulls>),
             'artist': (33, 63, <function fileinfo.stripnulls>),
             'comment': (97, 126, <function fileinfo.stripnulls>),
             'genre': (127, 128, <function ord>),
             'title': (3, 33, <function fileinfo.stripnulls>),
             'year': (93, 97, <function fileinfo.stripnulls>)}

   In [56]: m = fileinfo.MP3FileInfo()

   In [57]: m.tagDataMap
   Out[57]: {'album': (63, 93, <function fileinfo.stripnulls>),
             'artist': (33, 63, <function fileinfo.stripnulls>),
             'comment': (97, 126, <function fileinfo.stripnulls>),
             'genre': (127, 128, <function ord>),
             'title': (3, 33, <function fileinfo.stripnulls>),
             'year': (93, 97, <function fileinfo.stripnulls>)}

[54]:
    ``MP3FileInfo`` is the class itself, not any particular instance of the class.

[55]:
    ``tagDataMap`` is a class attribute: literally, an attribute of the class. It is available before
    creating any instance of the class.

[56]:
    Class attributes are available both through direct reference to the class and through any instance of
    the class.

.. note::

   * comparison with Java:

        - Java:
            
            both static variables (called class attributes in Python) and instance variables (called
            data attributes in Python) are defined immediately after the class definition (one with
            the ``static`` keyword, one without). 

        - Python:

            only class attributes can be defined here; data attributes are defined in the ``__init__`` 
            method.

   * Class attributes can be used as class-level constants, but they are not really constants. You can also
     change them.

Example 5.18 Modifying Class Attributes

.. sourcecode:: ipython
   :emphasize-lines: 4,19,24,27,30
   
   In [58]: class counter:
       ...:     count = 0
       ...:     def __init__(self):
       ...:         self.__class__.count += 1
       ...:         

   In [59]: counter
   Out[59]: __main__.counter

   In [60]: counter.count
   Out[60]: 0

   In [61]: c = counter()

   In [62]: c.count
   Out[62]: 1

   In [63]: counter.count
   Out[63]: 1

   In [64]: d = counter()

   In [65]: d.count
   Out[65]: 2

   In [66]: c.count
   Out[66]: 2

   In [67]: counter.count
   Out[67]: 2 

[58]:
    * ``count`` is a class attribute of the ``counter`` class

    * ``__class__`` is a built-in attribute of every class instance (of every class). It is a reference
      to the class that ``self`` is an instance of (in this case, the ``counter`` class).

      if ``self.__class__.count += 1`` changes to ``self.count += 1``, then the class attribute (``count``)
      would not be affected by the change made by the class instance

      .. sourcecode:: ipython
         :emphasize-lines: 4,19,24,27,30

         In [68]: class counter:
             ...:     count = 0
             ...:     def __init__(self):
             ...:         self.count += 1
             ...:         

         In [69]: counter
         Out[69]: __main__.counter

         In [70]: counter.count
         Out[70]: 0

         In [71]: c = counter()

         In [72]: c.count
         Out[72]: 1

         In [73]: counter.count
         Out[73]: 0

         In [74]: d = counter()

         In [75]: d.count
         Out[75]: 1

         In [76]: c.count
         Out[76]: 1

         In [77]: counter.count
         Out[77]: 0

[60]:
    Because ``count`` is a class attribute, it is available through direct reference to the class, before you have created any
    instance of the class.

[62]:
    Creating an instance of the class calls the ``__init__`` method, which increments the class attribute ``count`` by 1.
    This affects the class itself, not just the newly created instance.

    ( This only because ``self.__class__.count += 1``, if ``self.count += 1``, then the class itself would *not* be affected.)

[64]:
    Creating a second instance will increment the class attribute ``count`` again. Notice how the class attribute is shared by
    the class and all instances of the class.

.. _private_func:

5.9. Private Functions
----------------------

.. admonition:: how to

   If the name of a Python function, class method, or attribute starts with (*but doesn't end with*) two underscores, it's private;
   everything else is public.

   i.e., In ``MP3FileInfo``, there are two methods: ``__parse`` and ``__setitem__``. ``__parse`` is private, and ``__setitem__`` is
   public.

.. warning::

   In Python, all special methods (like ``__setitem__``) and built-in attributes (like ``__doc__``) follows a standard naming
   convention: they both starts with and end with two underscores. 

   Don't name your own methods and attributes this way, because it will only confuse you later.

Example 5.19 Trying to Call a Private Method

.. sourcecode:: ipython

   In [78]: import fileinfo

   In [79]: m = fileinfo.MP3FileInfo()

   In [80]: m.__parse("./Taylor Swift - State of Grace.mp3")
   ---------------------------------------------------------------------------
   AttributeError                            Traceback (most recent call last)
   <ipython-input-80-0195c2d23a2c> in <module>()
   ----> 1 m.__parse("./Taylor Swift - State of Grace.mp3")

   AttributeError: MP3FileInfo instance has no attribute '__parse'

   In [81]: m._MP3FileInfo__parse("./Taylor Swift - State of Grace.mp3") 

[80]:
    If you try to call a private method, Python will raise a slightly misleading exception, saying that the method does not exist.

[81]:
    Strictly speaking, private methods are accessible outside their class, just not *easily* accessible. 
    Nothing in Python is truly privatel internally, the names of private methods and attributes are mangled and unmangled on the fly
    to make them seem inaccessible by their given name.
