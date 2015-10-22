.. _chap6.rst:

============================
Exceptions and File Handling
============================

**Goal**:

* Catching exceptions with ``try...except``
* Protecting external resources with ``try...finally``
* Reading from files
* Assigning multiple values at once in a ``for`` loop
* Using the ``os`` module for all your cross-patform file manipulation needs
* Dynamically instantiating classes of unknown type by treating classes as objects and passing them around

.. _handling_exceptions:

6.1. Handling Exceptions
------------------------

Python uses ``try...except`` to handle exceptions and ``raise`` to generate them.

Java uses ``try...catch`` to handle exceptions, and ``throw`` to generate them.

Example 6.1. Opening a Non-Existent File

.. sourcecode:: ipython
   :linenos:  
 
   In [1]: fsock = open("/notthere","r")
   ---------------------------------------------------------------------------
   IOError                                   Traceback (most recent call last)
   <ipython-input-1-12d3ba34a1ce> in <module>()
   ----> 1 fsock = open("/notthere","r")

   IOError: [Errno 2] No such file or directory: '/notthere'

   In [2]: try:
      ...:     fsock = open("/notthere")
      ...: except IOError:
      ...:     print "The file does not exist, exiting gracefully"
      ...: print "This line will always print"
      ...: 
   The file does not exist, exiting gracefully
   This line will always print 

[2]:
    11. When the ``open`` method raises an ``IOError`` exception, you're ready for it. The ``except IOError:`` line catches the exception
        and executes your own block of code, which in this case just prints a more pleasant error message.

    13. Once an exception has been handled, processing continues normally on the first line after the ``try...except`` block.
        Note that this line will always print, whether or not an exception occurs. If you really did have a file called ``notthere`` in your
        root directiory, the call to ``open`` would succeed, the ``except`` clause would be ignored, and this line would still be executed.

6.1.1 Using Exceptions For other Purposes
*****************************************

a. Check whether the imported module work
+++++++++++++++++++++++++++++++++++++++++

A common use in the standard Python library is to try to import a module, and then check whether it worked.
(You can use this to define multiple levels of functionality based on which modules are available at run-time, or to support multiple platforms)

Example 6.2 Supporting Platform-Specific Functionality

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 8,11,14,16,17

   """ 
       this example shows how to use an exception to support platform-specific functionality
       this code comes from the getpass module, a wrapper module for getting a password from user 
   """

   # Bind the name getpass to the appropriate function
   try:
        import termios, TERMIOS
   except ImportError:
        try:
            import msvcrt
        except ImportError:
            try:
                from EasyDialogs import AskPassword
            except ImportError:
                getpass = default_getpass
            else:
                getpass = AskPassword
        else:
            getpass = win_getpass
   else:
        getpass = unix_getpass

[8]:
    ``termios`` is a UNIX-specific module that provides low-level control over the input terminal.
    If this module is not available (because it's not on your system, or your system doesn't support it),
    the import fails and Python raises an ``ImportError``, which you catch.
 
[11]:
    ``msvcrt`` is a Windows-specific module that provides an API to many useful functions in the Microsoft
    Visual C++ runtime services.

[14]:
    if the first two didn't work, you try to import a function from ``EasyDialogs``, which is a Mac OS-specific
    module that provides functions to pop up dialog boxes of various types.

[16]:
    None of these platform-specific modules is available, so you need to fall back on a default password input
    function (which is defined elsewhere in the ``getpass`` module). Notice what you're doing here: assigning the
    function ``default_getpass`` to the variable ``getpass``. If you read the official ``getpass`` documentation, it
    tells you that the ``getpass`` module defines a ``getpass`` function. It does this by binding ``getpass`` to the
    correct function for your platform. Then when you call the ``getpass`` function, you're really calling a 
    platform-specific function that this code has set up for you. You don't need to know which platform your code is 
    running on -- just call ``getpass``, and it will always do the right thing.

[17]:
    A ``try...except`` block can have an ``else`` clause. If no exception is raised during the ``try`` block, the
    ``else`` clause is executed afterwards. In this case, that means that the ``from EasyDialogs import AskPassword``
    import worked, so you should bind ``getpass`` to the ``AskPassword`` function.
 
b. define own exceptions
++++++++++++++++++++++++

You can also define your own exceptions by creating a class that inherits from the built-in ``Exception`` class, and
then raise your exceptions with the ``raise`` command.

You can find how to do it `here`__

__ pytut_

.. _working_with_file_obj:

6.2. Working with File Object
-----------------------------

6.2.1 Opening files
*******************

.. admonition:: Key Func
   
   ::

     open(file)

Example 6.3 Opening a File

.. sourcecode:: ipython
   :emphasize-lines: 1,3,6,9

   In [1]: f = open("./Music/Taylor Swift - State of Grace.mp3","rb")

   In [2]: f
   Out[2]: <open file './Music/Taylor Swift - State of Grace.mp3', mode 'rb' at 0x9132808>

   In [3]: f.mode
   Out[3]: 'rb'

   In [4]: f.name
   Out[4]: './Music/Taylor Swift - State of Grace.mp3'

[1]:
    * Python has a built-in function, ``open``, for opening a file on disk. 
       
    * The ``open`` method take up to three parameters: a filename, a mode, and a buffering parameter.
      Only the first one, filename, is required; the other two are optional. If not specific,
      the file is opened for reading in text mode.
      
      Here you are opening the file for reading in *binary* mode.

[2]:
    ``open`` returns a file object, which has methods and attributes for getting infomation
    about and manipulating the opened file.

[3]:
    The ``mode`` attribute of a file object tells you in which mode the file was opened.

[4]:
    The ``name`` attribute of a file object tells you the name of the file that the file object has open.

6.2.2 Reading Files
*******************

.. admonition:: Key Func
   
   ::

     f.tell(), f.seek(...), f.read(...)

Example 6.4. Reading a File

.. sourcecode:: ipython
   :emphasize-lines: 4,7,12,17

   In [5]: f
   Out[5]: <open file './Music/Taylor Swift - State of Grace.mp3', mode 'rb' at 0x9132808>

   In [6]: f.tell()
   Out[6]: 0L

   In [7]: f.seek(-128,2)

   In [8]: f.tell()
   Out[8]: 11934864L

   In [9]: tagData = f.read(128)

   In [10]: tagData
   Out[10]: 'TAGState of Grace\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Taylor Swift\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00State of Grace - Single\x00\x00\x00\x00\x00\x00\x002012\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02'

   In [11]: f.tell()
   Out[11]: 11934992L

[6]:
    The ``tell`` method of a file object tells you your current position in the open file. 
    Since you haven't done anything with this file yet, the current position is 0, which is the beginning of the file.

[7]:
    * The ``seek`` method of a file object moves to another position in the open file.
    
    * The second parameter specifies what the first one means:
        
        - ``0`` means move to an absolute position (counting from the start of the file)
        - ``1`` means move to a relative position (counting from the current position)
        - ``2`` means move to a position relative to the end of the file.

    * Since the MP3 tags you're looking for are stored at the end of the file, you use ``2``
      and tell the file object to move to a position ``128`` bytes from the end of the file.

[9]:
    * The ``read`` method reads a specified number of bytes from the open file
      and returns a string with the data that was read.

    * The optional parameter specifies the maximum number of bytes to read. 
      If no parameter is specified, ``read`` will read until the end of the file.

    * The read data is assigned to the ``tagData`` variable, and the current position
      is updated based on how many bytes were read.

[11]:
    The ``tell`` method confirms that the current position has moved. If you do the math,
    you'll see that after reading 128 bytes, the position has been incremented by 128.

6.2.3 Closing Files
*******************

Open files consume system resourcesm and depending on the file mode, other programs may not
be able to access them. It's important to close files as soon as you're finished with them.

Example 6.5 Closing a File

.. sourcecode:: ipython
   :emphasize-lines: 4,7,15,39

   In [12]: f
   Out[12]: <open file './Music/Taylor Swift - State of Grace.mp3', mode 'rb' at 0x9132808>

   In [13]: f.closed
   Out[13]: False

   In [15]: f.close()

   In [16]: f
   Out[16]: <closed file './Music/Taylor Swift - State of Grace.mp3', mode 'rb' at 0x9132808>

   In [17]: f.closed
   Out[17]: True

   In [18]: f.seek(0)
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-18-d0cb2b3c0dfb> in <module>()
   ----> 1 f.seek(0)

   ValueError: I/O operation on closed file

   In [19]: f.tell()
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-19-322ae27c0b94> in <module>()
   ----> 1 f.tell()

   ValueError: I/O operation on closed file

   In [20]: f.read()
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-20-bacd0e0f09a3> in <module>()
   ----> 1 f.read()

   ValueError: I/O operation on closed file

   In [21]: f.close()

[13]:
    The ``closed`` attribute of a file object indicates whether the object has a file open or not.
    In this case, the file is still open (``closed`` is ``False``)

[15]:
    To close a file, call the ``close`` method of the file object. This frees the lock (if any) that
    you were holding on the file, flushes buffered writes (if any) that the system hadn't gotten
    around to actually wiriting yet, and releases the system resources.

[18]:
    Just because a file is closed doesn't mean that the file object ceases to exist. The variable ``f``
    will continue to exist until it goes out of scope or gets manually deleted. However, none of the 
    methods that manipulate an open file will work once the file has been closed;
    they will raise an exception.

[21]:
    Calling ``close`` on a file object whose file is already closed does *not* raise an exception.

6.2.4 Handling I/O Errors
**************************

Example 6.6 File Objects in MP3FileInfo

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 3,4,6,7,8

   # this example shows how to safely open and read from a file and gracefully handle errors.

   try:
        fsock = open(filename, "rb", 0)
        try:
            fsock.seek(-128,2)
            tagdata = fsock.read(128)
        finally:
            fsock.close()
        .
        .
        .
   except IOError:
        pass

[3]:
    Because opening and reading files is risky and may raise an exception, 
    all of this code is wrapped in a ``try...except`` block.

[4]:
    The ``open`` function may raise an ``IOError``. (Maybe the file doesn't exist)

[6]:
    The ``seek`` method may raise an ``IOError``. (Maybe the file is smaller than 128 bytes)

[7]:
    The ``read`` method may raise an ``IOError``. (Maybe the disk has a bad sector, or it's on a network drive and the network just went down)

[8]:
    ``try...finally`` block:
        
        * code in the ``finally`` block will *always* be executed, even if something in the ``try`` block raises an exception.

6.2.5 Writing to Files
**********************

There are two basic file modes:
    
    * "Append" (``a``) mode will add data to the end of the file.
    * "write" (``w``) mode will overwrite the file.

Either mode will create the file automatically if it doesn't already exist.

Example 6.7. Writing to Files

.. sourcecode:: ipython
   :emphasize-lines: 1,3,7,10,16

   In [22]: logfile = open('test.log','w')

   In [23]: logfile.write('test succeeded')

   In [24]: logfile.close()

   In [25]: print file('test.log').read()
   test succeeded

   In [26]: logfile = open('test.log','a')

   In [27]: logfile.write('line 2')

   In [28]: logfile.close()

   In [29]: print file('test.log').read()
   test succeededline 2

[21]:
    opening the file for writing. (The second parameter ``w`` means open the file for writing).
    The previous contents of that file has gone now.

[23]:
    You can add data to the newly opened file with the ``write`` method of the file object returned by ``open``.

[25]:
    ``file`` is a synonym for ``open``. This one-liner opens the file, reads its contents, and prints them.

[26]:
    open the file and append to it. (The ``a`` parameter means open the file for appending.)
    Appending will *never* harm the existing contents of the file.

[29]:
    Note that carriage returns are not included. Since you didn't write them explicitly to the file either time,
    the file doesn't include them. You can write a carriage return with the ``\n`` character.
    Since you didn't do this, everything you wrote to the file ended up smooshed together on the same line.

.. _iterating_loops:

6.3.  Iterating with for Loops
------------------------------

Most other languages don't have a powerful list datatype like Python,
so you end up doing a lot of manual work, specifying a start, end, and step to define a range of integers or character or other iteratable entities.
But in Python, a ``for`` loop simply iterates over a lis, the same way list comprehensions work.

Example 6.8 Introducing the ``for`` loop

.. sourcecode:: ipython
   :emphasize-lines: 3,10

   In [1]: li = ['a','b','e']

   In [2]: for s in li:
      ...:     print s
      ...:     
   a
   b
   e

   In [3]: print "\n".join(li)
   a
   b
   e

[2]:
    The syntax for a ``for`` loop is similar to list comprehensions. ``li`` is a list, 
    and ``s`` will take the value of each element in turn, starting from the first element.

Example 6.9 Simple counters

.. sourcecode:: ipython
   :emphasize-lines: 1

   In [5]: for i in range(5):
      ...:     print i
      ...:     
   0
   1
   2
   3
   4

``for`` loops are not just for simple counters. They can iterate through all kinds of things.

Example 6.10 Iterating Through a Dictionary

.. sourcecode:: ipython
   :emphasize-lines: 3, 14
    
   In [8]: import os

   In [9]: for k,v in os.environ.items():
      ...:     print "%s=%s" % (k,v)
      ...:     
   XAUTHORITY=/home/zeyuan_hu/.Xauthority
   GNOME_DESKTOP_SESSION_ID=this-is-deprecated
   LESSOPEN=| /usr/bin/lesspipe %s
   LOGNAME=zeyuan_hu
   USER=zeyuan_hu
   
   [...snip...]

   In [10]: print "\n".join(["%s=%s" % (k,v) for k,v in os.environ.items()])
   XAUTHORITY=/home/zeyuan_hu/.Xauthority
   GNOME_DESKTOP_SESSION_ID=this-is-deprecated
   LESSOPEN=| /usr/bin/lesspipe %s
   LOGNAME=zeyuan_hu
   USER=zeyuan_hu

   [...snip...]

[9]:
    * ``os.environ`` is a dictionary of the environment variables defined on your system.
 
    * ``os.environ.items()`` returns a list of tuples: ``[(key1, value1), (key2, value2), ...]``

[10]:
    this version is slightly faster, because there is only one ``print`` statement instead of many.

Example 6.11 for loop in MP3FileInfo

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 6,11

   tagDataMap = {"title"   : (  3,  33, stripnulls),
                 "artist"  : ( 33,  63, stripnulls),
                 "album"   : ( 63,  93, stripnulls),
                 "year"    : ( 93,  97, stripnulls),
                 "comment" : ( 97, 126, stripnulls),
                 "genre"   : (127, 128, ord)}
   .
   .
   .
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])

[6]:
    ``tagDataMap`` is a class attribute that defines the tags you're looking for in an MP3 file.
    
    .. admonition:: fact about tags in MP3 file
    
       Tags are stored in fixed-length fields. 

       Once you read the last 128 bytes of the file, bytes 3 through 32 of those are always the 
       song title, 33 through 62 are always the artist name, 63 through 92 are the album name, and so forth.

[11]:
   The structure of the ``for`` variables matches the structure of the elements of the list returned by ``items``.
   Remember that ``items`` returns a list of tuples of the form ``(key, value)``. The first element of the list
   is ``("title", (3, 33, <function stripnulls>))``, so the first time around the loop, tag gets ``title``, ``start``
   gets ``3``, ``end`` gets ``33``, and ``parseFunc`` gets the function ``stripnulls``.

.. _sys.modules:

6.4. Using *sys.modules*
-------------------------

Modules, like everything else in Python, are objects.
Once imported, you can always get a reference to a module through the global dictionary ``sys.modules``.

Example 6.12 Introducing ``sys.modules``

.. sourcecode:: ipython
   :emphasize-lines: 1,3
   
   In [3]: import sys

   In [4]: print '\n'.join(sys.modules.keys())
   copy_reg
   sre_compile
   _sre
   encodings
   site
   __builtin__
   sys
   __main__
   encodings.encodings
   abc
   posixpath
   _weakrefset
   errno
   re
   os

[3]:
    The ``sys`` module contains system-level information, such as the version of Python you're running 
    (``sys.version`` or ``sys.version_info``)

[4]:
    ``sys.modules`` is a dictionary containing all the modules that have ever been imported since Python
    was started; the key is the module name, the value is the module object.

Example 6.13 Using sys.modules

.. sourcecode:: ipython
   :emphasize-lines: 1,24
   
   In [13]: import fileinfo

   In [14]: print '\n'.join(sys.modules.keys())
   copy_reg
   fileinfo
   sre_compile
   _sre
   encodings
   site
   __builtin__
   sys
   __main__
   encodings.encodings
   abc
   posixpath
   _weakrefset
   errno
   re
   os

   In [15]: fileinfo
   Out[15]: <module 'fileinfo' from 'fileinfo.pyc'>

   In [16]: sys.modules["fileinfo"]
   Out[16]: <module 'fileinfo' from 'fileinfo.pyc'>

[13]:
    As new modules are imported, they are added to ``sys.modules``.

[16]:
    Given the name (as a string) of any previously-imported module, 
    you can get a reference to the module itself through the ``sys.modules`` dictionary.

Example 6.14 The __module__ Class Attribute

.. sourcecode:: ipython
   :emphasize-lines: 3,6

   In [17]: from fileinfo import MP3FileInfo

   In [18]: MP3FileInfo.__module__
   Out[18]: 'fileinfo'

   In [19]: sys.modules[MP3FileInfo.__module__]
   Out[19]: <module 'fileinfo' from 'fileinfo.pyc'>

[18]:
    Every Python class has a built-in class attribute __module__, which is the name of the module in which the class is defined.

[19]:
    Combining this with the ``sys.modules`` dictionary, you can get a reference to the module in which a class is defined.

.. _working_with_directories:

6.5. Working with Directories
-----------------------------

.. admonition:: Key Func

   .. sourcecode:: python
    
      os.path.join(path, filename),
      os.path.expanduser(pathname including "~")
    
      path, filename = os.path.split(pathname)
      filename, fileext = os.path.splitext(filename)

      os.listdir(pathname)
      os.path.isfile(pathname)
      os.path.isdir(pathname)
      os.getcwd()
      os.path.normcase(file or folder)
    
      glob module


6.5.1 Constructing Pathnames
****************************

Example 6.16 Constructing Pathnames

.. sourcecode:: ipython
   :emphasize-lines: 3,6,9,12

   In [21]: import os

   In [22]: os.path.join("../Music/","Taylor Swift - State of Grace.mp3")
   Out[22]: '../Music/Taylor Swift - State of Grace.mp3'

   In [23]: os.path.join("../Music","Taylor Swift - State of Grace.mp3")
   Out[23]: '../Music/Taylor Swift - State of Grace.mp3'

   In [24]: os.path.expanduser("~")
   Out[24]: '/home/zeyuan_hu'

   In [25]: os.path.join(os.path.expanduser("~"),"Python")
   Out[25]: '/home/zeyuan_hu/Python'

[22]:
    ``os.path`` is a reference to a module -- which module depends on your platform.
    Just as ``getpass`` encapsulates differences between platforms by setting ``getpass`` to a platform-specific function,
    ``os`` encapsulates differences between platforms by setting ``path`` to a platform-specific module.

[23]:
    ``join`` will add an extra backslash to the pathname before joining it to the filename.

.. sourcecode:: python

    # constructs a pathname out of one or more partial pathnames.
    os.path.join(path, filename)

    # expand a pathname that uses ~ to represent the current user's home directory
    os.path.expanduser(path including "~")

6.5.2 Splitting Pathnames
*************************

Example 6.17 Splitting Pathnames

.. sourcecode:: ipython
   :emphasize-lines: 1, 4, 6, 9, 12

   In [26]: os.path.split('../Music/Taylor Swift - State of Grace.mp3')
   Out[26]: ('../Music', 'Taylor Swift - State of Grace.mp3')

   In [27]: filepath, filename = os.path.split('../Music/Taylor Swift - State of Grace.mp3')

   In [28]: filepath
   Out[28]: '../Music'

   In [29]: filename
   Out[29]: 'Taylor Swift - State of Grace.mp3'

   In [30]: shortname, extension = os.path.splitext(filename)

   In [31]: shortname
   Out[31]: 'Taylor Swift - State of Grace'

   In [32]: extension
   Out[32]: '.mp3'

.. sourcecode:: python
   
   # splits a full pathname and returns a tuple containing the path and filename.
   # you can assign the return value of split function into a tuple of two variables.
   path, filename = os.path.split(pathname)

   # splits a filename and returns a tuple containing the filename and the file extension
   filename, fileext = os.path.splitext(filename)

6.5.3 Listing Directories
*************************

Example 6.18 Listing Directories

.. sourcecode:: ipython
   :emphasize-lines: 6,12,18
   
   In [35]: os.path.expanduser("~")
   Out[35]: '/home/zeyuan_hu'

   In [36]: dirname = os.path.expanduser("~")

   In [37]: os.listdir(dirname)
   Out[37]: 
   ['.pip','.adobe','.gconf','.gnome2','.xscreensaver','Dropbox',
    'Music','.profile','py','Videos','.pki','.dropbox','.swp',
    '.cache'.'.Xauthority','Documents','.vim', ... ]

   In [38]: [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
   Out[38]: 
   ['.dmrc', '.swp','.Xauthority','.pam_environment','.bash_history',
    '.gksu.lock','.install4j','.viminfo','.pulse-cookie','examples.desktop',
    '.vimrc~','.bashrc','.vimrc', ...]

   In [39]: [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,f))]
   Out[39]: 
   ['Downloads','.matplotlib','.pip','.gnome2','.java','Dropbox','Music',
    'py','Videos','.dropbox','.cache','Documents','.vim','Desktop',
    'Public','Ubuntu One','Templates','Pictures','.ssh', ... ]
   
.. sourcecode:: python

   # takes a pathname and returns a list of the contents of the directory
   # note that listdir returns both files and folders, with no indication of which is which.
   os.listdir(pathname)

   # used to separate the files from the folders
   # takes a pathname and returns 1 if the path represents a file, and 0 otherwise.
   # also works with a partial path, relative to the current working directory.
   os.path.isfile(pathname)

   # get the current working directory
   os.getcwd()

   # used to get a list of the subdirectories within a directory
   # takes a pathname and returns 1 if the path represents a directory, and 0 otherwise.
   os.path.isdir(pathname)

Example 6.19 Listing Directories in fileinfo.py

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 3,5

   def listDirectory(directory, fileExtList):
       "get list of file info objects for files of particular extensions"
        fileList = [os.path.normcase(f) for f in os.listdir(directory)]

        fileList = [os.path.join(directory, f) for f in fileList if os.path.splitext(f)[1] in fileExtList]

[3]:
    ``normcase`` is a useful little function that compensates for case-insensitive operation systems that
    think that ``mahadeva.mp3`` and ``mahadeva.MP3`` are the same file. For instance, on Windows and Mac OS,
    ``normcase`` will convert the entire filename to lowercase; on UNIX-compatible systems, it will return the
    filename unchanged.

[5]:
    * Iterating through the normalized list with ``f`` again, you use ``os.path.splitext(f)`` to split each filename
      into name and extension.

    * For each file, you see if the extension is in the list of file extensions you care about (``fileExtList``, which
      was passed to the ``listDirectory`` function).

.. sourcecode:: python

   # normalize the case according to operating system defaults
   os.path.normcase(file or folder)

.. note::

   Whenever possible, you should use the functions in ``os`` and ``os.path`` for file, directory, and path manipulations.
   Those modules are wrappers for platform-specific modules, so function like ``os.path.split`` work on UNIX, Windows, Mac OS,
   and any other platform supported by Python.

Example 6.20 Listing Directories with glob

.. sourcecode:: ipython
   :emphasize-lines: 7,15,19

   In [42]: os.listdir("/home/zeyuan_hu/Music")
   Out[42]: ['a_time_long_forgotten_con.mp3', 'hellraiser.mp3','kairo.mp3',
             'long_way_home1.mp3', 'sidewinder.mp3','spinning.mp3']

   In [43]: import glob

   In [44]: glob.glob("/home/zeyuan_hu/Music/*.mp3")
   Out[44]: ["/home/zeyuan_hu/Music/a_time_long_forgotten_con.mp3",
             "/home/zeyuan_hu/Music/hellraiser.mp3",
             "/home/zeyuan_hu/Music/kairo.mp3",
             "/home/zeyuan_hu/Music/long_way_home1.mp3",
             "/home/zeyuan_hu/Music/sidewinder.mp3",
             "/home/zeyuan_hu/Music/spinning.mp3"]

   In [45]: glob.glob("/home/zeyuan_hu/Music/s*.mp3")
   Out[45]: ["/home/zeyuan_hu/Music/sidewinder.mp3",
             "/home/zeyuan_hu/Music/spinning.mp3"]

   In [46]: glob.glob("/home/zeyuan_hu/*/*.mp3")
  
[44]:
    The ``glob`` module, takes a wildcard and returns the full path of all files and
    directories matching the wildcard. Here the wildcard is a directory path plus "\*.mp3",
    which will match all ``.mp3`` files. Note that each element of the returned list already
    includes the full path of the file.

[45]:
    If you want to find all the files in a specific directory that start with "s" and end with
    ".mp3", you can do that too.

[46]:
    Now consider this scenario: you have a music directory, with several subdirectories within it,
    with ``.mp3`` files within each subdirectory. You can get a list of all of those with a single call
    to ``glob``, by using two wildcards at once. One wildcard is the "\*.mp3" (to match ``.mp3`` files), 
    and one wildcard is *within the directory path itself*, to match any subdirectory within ``/home/zeyuan_hu/``.

.. _all_together:

6.6. Putting it All Together
----------------------------

Example 6.21. listDirectory

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 1, 5, 7, 9, 10, 12

   def listDirectory(directory, fileExtList):
       "get list of file info objects for files of particular extensions"
        fileList = [os.path.normcase(f) for f in os.listdir(directory)]

        fileList = [os.path.join(directory, f) for f in fileList if os.path.splitext(f)[1] in fileExtList]

        def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
            "get file info class from filename extension"
            subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
            return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

        return [getFileInfoClass(f)(f) for f in fileList]

[1]:
    ``listDirectory`` is the main attraction of this entire module. It takes a directory(i.e. /home/zeyuan_hu/Music/)
    and a list of interesting file extensions (i.e. ``['.mp3']``), and it returns a list of class instances that act
    like dictionaries that contain metadata about each interesting file in that directory.

[5]:
    This line of code gets a list of the full pathnames of all the files in ``directory`` that have an interesting file
    extension (as specified by ``fileExtList``).

[7]:
    Python supports *nest functions*:
        
        The nested function ``getFileInfoClass`` can be called only from the function in which it is defined, ``listDirectory``.

[7]:
    This is a function with two arguments; ``filename`` is required, but ``module`` is optional and defaults to the module
    that contains the ``FileInfo`` class.

[9]:
    This line of code gets the extension of the file (``os.path.splitext(filename)[1]``), forces it to uppercase(``.upper()``),
    slice off the dot (``[1:]``), and constructs a class name out of it with string formatting. So ``/home/zeyuan_hu/Music/mahadeva.mp3``
    becomes ``.mp3`` becomes ``.MP3`` becomes ``MP3`` becomes ``MP3FileInfo``.

[10]:
    Having constructed the name of the handler class that would handle this file, you check to see if that handler class actually
    exists in this module. If it does, you return the class, otherwise you return the base class ``FileInfo``. 
   
    This is s a very important point: *this function returns a class.* Not an instance of a class, but the class itself.

[12]:
    For each file in the "interesting files" list (``fileList``), you call ``getFileInfoClass`` with the filename(``f``).
    Calling ``getFileInfoClass(f)`` returns a class; 
    You then create an instance of this class and pass the filename(``f`` again), to the ``__init__`` method.
    As you saw earlier in this chapter, the ``__init__`` method of ``FileInfo`` sets ``self["name"]``, which triggers 
    ``__setitem__``, which is overridden in the descendant (``MP3FileInfo``) to parse the file appropriately to pull out
    the file's metadata. You do all that fo each interesting file and return a list of the resulting instances.

.. note::

   Note that ``listDirectory`` is completely generic. It doesn't know ahead of time which types of files it will be getting,
   or which classes are defined that could potentially handle those files. It inspects the directory for the files to 
   process, and then introspects its own module to see what special handler classes (like ``MP3FileInfo``) are defined.
   
   You can extend this program to handle other types of files simply by defining an appropriately-named class:
   ``HTMLFileInfo`` for HTML files, ``DOCFileInfo`` for Word ``.doc`` files., and so forth.

   ``listDirectory`` will handle them all, without modification, by handing off the real work to the appropriate classes and collating the results.







.. include:: ../../../links.rst
