.. _chap7.rst:

==================
Regular Expression
==================

.. admonition:: usage
   
   Regular expressions are a powerful and standardized way of searching, replacing, and
   parsing text with complex patterns of characters.

"Some people, when confronted with a problem, think "I know, I'll use regular expressions."
Now they have two problems."

-- **Jamie Zawinski**, in `comp.emacs.xemacs`_

.. _comp.emacs.xemacs: http://groups.google.com/groups?selm=33F0C496.370D7C45%40netscape.com

**Goal**:

* ``^`` matches the beginning of a string.
* ``$`` matches the end of a string.
* ``\b`` matches a word boundary.
* ``\d`` matches any numeric digit.
* ``\D`` matches any non-numeric character.
* ``x?`` matches an *optional* ``x`` character (in other words, it matches an ``x`` zero or *one* times).
* ``x*`` matches ``x`` zero or *more* times.
* ``x+`` matches ``x`` one or more times.
* ``x{n,m}`` matches an ``x`` character at least ``n`` times, but not more than ``m`` times.
* ``(a|b|c)`` matches either ``a`` or ``b`` or ``c``.
* ``(x)`` in general is a *remembered group*. You can get the value of what matched by using the ``groups()``
  method of the object returned by ``re.search``.


.. _diving_in7:

7.1. Diving In
--------------

7.1.1 Limitation of String Methods
**********************************

String have methods of searching (``index``, ``find``, and ``count``), replacing (``replace``), and 
parsing (``split``), but they are limited to the simplest of cases:

    The search methods look for *a single, hard-coded substring*, and they are always *case-sensitive*.
    Those limitations are also true for replacing method and parsing method.

7.1.2 When to Use Regular Expressions
*************************************

If what you're trying to do can be accomplished with string functions, you should use them. 
They're fast and simple and easy to read.

But if you find yourself using a lot of different string functions with ``if`` statements to handle
special cases, or if you're combining them with ``split`` and ``join`` and list comprehensions in
weird unreadable ways, you may need to move up to regular expressions.

7.1.3 Python and Regular Expressions
************************************

Regular expressions are supported by ``re`` module. You can get an overview of the available functions
and their arguments by just reading the summary of the `re`_ module.


.. _case_study_street:

7.2. Case Study: Street Addresses
---------------------------------

This series of examples was inspired by a real-life problem I had in my day job several years ago,
when I needed to scrub and standardize street addresses exported from a legacy system before importing
them into a newer system.

7.1.1 ``^`` and ``$``
**********************

Example 7.1 Matching at the End of a String

.. admonition:: Key Expression
   
   * ``^`` matches the beginning of a string.
   * ``$`` matches the end of a string.

.. admonition:: Key Func
   
   ::

     re.sub(pattern, repl, string) 

.. sourcecode:: ipython
   :emphasize-lines: 14, 16

   In [1]: s = '100 NORTH MAIN ROAD'

   In [2]: s.replace('ROAD', 'RD.')
   Out[2]: '100 NORTH MAIN RD.'

   In [3]: s = '100 NORTH BROAD ROAD'

   In [4]: s.replace('ROAD', 'RD.')
   Out[4]: '100 NORTH BRD. RD.'

   In [5]: s[:-4] + s[-4:].replace('ROAD','RD.')
   Out[5]: '100 NORTH BROAD RD.'

   In [6]: import re

   In [7]: re.sub('ROAD$', 'RD.', s)
   Out[7]: '100 NORTH BROAD RD.'  

[2]:
    My goal is to standardize a street address so that ``'ROAD'`` is always abbreviated as ``'RD.'``.
    At first glance, I thought this was simple enough that I could just use the string method ``replace``. 

[4]:
    Life, unfortunately, is full of counterexamples, and this is the one. The problem here is that ``'ROAD'``
    appears twice in the address, once as part of the street name ``'BROAD'`` and once as its own word.
    The ``replace`` method sees these two occurrences and blindly replaces both of them; addresses getting destroyed.

[5]:
    To solve the problem of addresses with more than one ``'ROAD'`` substring, you could resort to something like this:
    
        only search and replace ``'ROAD'`` in the last four characters of the address (``s[-4:]``), and leave the string
        alone (``s[:-4]``).

     But you can see that this is not a general approach: 

        for example, the pattern is dependent on the length of the string you're replacing (if you were replacing
        ``'STREET'`` with ``'ST.'``, you would need to use ``s[:-6]`` and ``s[-6:].replace(...)``).

[6]:
    It's time to move up to regular expressions.
    In Python, all functionality related to regular expressions is contained in the ``re`` module.

[7]:
    * ``'ROAD$'``:
        - This is a simple regular expression that matches ``'ROAD'`` only when it occurs at the end of a string.

        - The ``$`` means "end of the string". (the corresponding character, ``^``, which means "beginning of the string")

    * ::
       
        # you search the string 's' for the regular expression 'ROAD$' and replace it with 'RD.'
        re.sub(pattern, repl, string)

    * This matches the ``ROAD`` at the end of the string ``s``, but does *not* match the ``ROAD`` that's part of the word
      ``BROAD``, because tha's in the middle of ``s``

.. admonition:: problem
    
   Not all addresses included a street designation at all; some just ended with the street name. If the street name was 
   ``'BROAD'``, then the regular expression would match ``'ROAD'`` at the end of the string as part of the word
   ``'BROAD'``. which is not what I wanted.

7.1.2 ``\b`` and ``r``
**********************

Example 7.2 Matching Whole Words

.. admonition:: Key Expression

   * ``\b`` matches a word boundary
   * raw string: prefix the string with the letter ``r``.

.. sourcecode:: ipython
   :emphasize-lines: 9,17

   In [13]: s = '100 BROAD'

   In [14]: re.sub('ROAD$', 'RD.', s)
   Out[14]: '100 BRD.'

   In [15]: re.sub('\\bROAD$', 'RD.', s)
   Out[15]: '100 BROAD'

   In [16]: re.sub(r'\bROAD$', 'RD.', s)
   Out[16]: '100 BROAD'

   In [17]: s = '100 BROAD ROAD APT.3'

   In [18]: re.sub(r'\bROAD$', 'RD.', s)
   Out[18]: '100 BROAD ROAD APT.3'

   In [19]: re.sub(r'\bROAD\b', 'RD.', s)
   Out[19]: '100 BROAD RD. APT.3' 

[14]:
    problem in the previous approach

[15]:
    * What I really want was to match ``'ROAD'`` when it was at the end of the string and
      it was its own whole word, not a part of some larger word.

    * ``\b``:
        - means "a word boundary must occur right here."
        - In Python, this is complicated by the fact that the ``'\'`` character in a string must itself be escaped.
          (this is called *backslash plague*)
    
    * ``r``:
        - to work around the backslash plague, you can use what is called a raw string, 
          by prefixing the string with the letter ``r``.

        - this tells Python that nothing in this string should be escaped.

        - ie. ``'\t'`` is a tab character, but ``r'\t'`` is really the backslash character ``\`` followed by the
          letter ``t``.
 
        - .. admonition:: Tip
              
             Always using raw strings when dealing with regular expressions.

[18]:
    .. admonition:: problem

       I soon found more cases that contradicted my logic. 
       In this case, the street address contained the word ``'ROAD'`` as a whole word by itself, but it
       wasn't at the end, because the address had an apartment number after the street designation.
       Because ``'ROAD'`` isn't at the very end of the string, it doesn't match, so the entire call to 
       ``re.sub`` ends up replacing nothing at all, and you get the original string back, which is 
       not what you want.

[19]:
    To Solve this problem, I removed the ``$`` character and added another ``\b``.

    Now the regular expression reads "match ``'ROAD'`` when it's whole word by itself anywhere in the string," 
    whether at the end, the beginning, or somewhere in the middle.

.. _case_study_roman:

7.3. Case Study: Roman Numerals
-------------------------------

7.3.0 Introduction to Roman Numerals
************************************

You've most likely seen Roman numerals, even if you didn't recognize them. You may have seen them in the copyrights of 
old movies and television shows ("Copyright ``MCMXLVI``" instead of "Copyright ``1946``"), or on the dedication walls of 
libraries or universities ("established ``MDCCCLXXXVIII``" instead of "established ``1888``"). You may also have seen them
in outlines and bibliographical references. It's a system of representing numbers that really does date back to the 
ancient Roman empire.

7.3.0.0 Rules in Roman Numerals
+++++++++++++++++++++++++++++++

* there are seven characters that are repeated and combined in various ways to represent numbers:
    - ``I`` = 1
    - ``V`` = 5
    - ``X`` = 10
    - ``L`` = 50
    - ``C`` = 100
    - ``D`` = 500
    - ``M`` = 1000

* Characters are additive:
    ``I`` is ``1``, ``II`` is 2, and ``III`` is 3. ``VI`` is ``6`` (literally, "5 and 1"), ``VII`` is ``7``, and
    ``VIII`` is ``8``.

* Subtraction rule:
    - A smaller number in front of a larger number means subtraction, all else means addition:
        ``IV`` means ``4``, ``VI`` means ``6``

    - You would not put more than one smaller number in front of a larger number to subtract:
        ``IIV`` would not mean ``3``, and it is not even a valid Roman numeral.

    - You must separates ones, tens, hundreds, and thousands as separate items:
        + That means that ``99`` is ``XCIX`` ("90 plus 9"), but never should be written as ``IC``.
        + Similarly, ``999`` cannot be ``IM`` and ``1999`` cannot be ``MIM``

* The tens characters (``I``, ``X``, ``C``, and ``M``) can be repeated up to three times: (except ``M``, which could be repeated up to *four* times)
    - At ``4``, cannot represent it as ``IIII``; instead, it is represented as ``IV`` ( "1 less than 5")

    - Number ``40`` is written as ``XL`` (10 less than 50), ``41`` as ``XLI``, ``42`` as ``XLII``, ``43`` as ``XLIII``,
      and then ``44`` as ``XLIV`` (10 less than 50, then 1 less than 5).

    - Similarly, at ``9``, you need to subtract from the next highest tens character: ``8`` is ``VIII``, but ``9`` is ``IX``
      (1 less than 10), not ``VIIII``. The number ``90`` is ``XC``, ``900`` is ``CM``.

* The fives characters cannot be repeated:
    - Number ``10`` is always represented as ``X``, never as ``VV``.

    - Number ``100`` is always ``C``, never ``LL``.

* Roman numerals are always written highest to lowest, and read left to right, so the order of characters matters very much:
    - ``DC`` is ``600``; ``CD`` is a completely different number(``400``, 100 less than 500).

    - ``CI`` is ``101``; ``IC`` is not even a valid Roman numeral (because you cannot subtract 1 directly from 100; you
      would need to write it as ``XCIX``, for 10 less than 100, then 1 less than 10).

7.3.1 Validating Roman Numeral
******************************

Goal:
    Validating that an arbitrary string is a valid Roman numeral.

Approach:
    One digit at a time

7.3.1.0 Checing for Thousands ``?``
+++++++++++++++++++++++++++++++++++++

Since Roman numerals are always written highest to lowest, let's start with the highest: the thousands place.

For numbers 1000 and higher, the thousands are represented by a series of ``M`` characters.

Example 7.3 Checking for Thousands

.. admonition:: Key Expression

   ``x?`` matches an *optional* ``x`` character (in other words, it matches an ``x`` zero or *one* times).

.. admonition:: Key Func
    
   ::

     re.search(pattern, string)


.. sourcecode:: ipython
   :emphasize-lines: 3,5

   In [20]: import re

   In [21]: pattern = '^M?M?M?M?$'

   In [22]: re.search(pattern, 'M')
   Out[22]: <_sre.SRE_Match at 0x92c5b48>

   In [23]: re.search(pattern, 'MM')
   Out[23]: <_sre.SRE_Match at 0x92c5bf0>
   In [24]: re.search(pattern,'MMM')
   Out[24]: <_sre.SRE_Match at 0x92c5d08>

   In [25]: re.search(pattern,'MMMMM')

   In [26]: re.search(pattern,'')
   Out[26]: <_sre.SRE_Match at 0x92c5e58>

[21]:
    This pattern has three parts:

        - ``^`` to match what following only at the beginning of the string. If this were not specified, the pattern
          would match no matter where the ``M`` characters were, which is not what you want. You want to make sure
          that the ``M`` characters, if they're there, are at the beginning of the string.

        - ``M?`` to optionally match a single ``M`` character. Since this is repeated three times, you're matching 
          anywhere from zero to three ``M`` characters in a row.

        - ``$`` to match what precedes only at the end of the string. When combined with the ``^`` character at the
          beginning, this means that the pattern must match the entire string, with no other characters before or
          after the ``M`` characters.

[22]: 
    * re.search::
        
        # takes a regular expression (pattern) and a string (M) to try to match against the regular expression. 
        # If a match is found, search returns an object which has various methods to describe the match
        # If no match is found, search returns None, the Python null value.
        re.search(pattern, string)

    * ``'M'`` matches, because the first optional ``M`` matches and the second and third optional ``M`` characters are ignored.

[25]:
    ``'MMMM'`` does not match. All four ``M`` characters match, but then the regular expression insisits on the string
    ending (because of the ``$`` character), and the string doesn't end yet (because of the fourth ``M``). So ``search`` 
    returns ``None``.

[26]:
    Interestingly, an empty string also matches this regular expression, since all the ``M`` characters are optional.

7.3.1.1 Checking for Hundreds ``(a|b|c)``
+++++++++++++++++++++++++++++++++++++++++

The hundreds place is more difficult than the thousands, because there are several mutually exclusive ways it would be
expressed, depending on its value.

    * ``100`` = ``C``
    * ``200`` = ``CC``
    * ``300`` = ``CCC``
    * ``400`` = ``CD``
    * ``500`` = ``D``
    * ``600`` = ``DC``
    * ``700`` = ``DCC``
    * ``800`` = ``DCCC``
    * ``900`` = ``CM``

So there are three possible patterns:

    * ``CM``
    * ``CD``
    * an optional ``D``, followed by zero to three ``C`` characters:
        
        - Zero to three ``C`` characters (zero if the hundreds place is 0)
        - ``D``, followed by zero to three ``C`` characters.

Example 7.4. Checking for Hundreds

.. admonition:: Key Expression

   ``(a|b|c)`` matches either ``a`` or ``b`` or ``c``.

.. sourcecode:: ipython
   :emphasize-lines: 3

   In [27]: import re

   In [28]: pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)$'

   In [29]: re.search(pattern,'MCM')
   Out[29]: <_sre.SRE_Match at 0x9248820>

   In [30]: re.search(pattern,'MD')
   Out[30]: <_sre.SRE_Match at 0x92487a0>

   In [31]: re.search(pattern,'MMMCCC')
   Out[31]: <_sre.SRE_Match at 0x9248760>

   In [32]: re.search(pattern,'MCMC')

   In [33]: re.search(pattern,'')
   Out[33]: <_sre.SRE_Match at 0x92488e0> 

[28]:
    This pattern starts out the same as the previous one, checking for the beginning of the string (``^``),
    then the thousands place (``M?M?M?M?``). Then it has the new part, in parentheses, which defines a set of 
    three mutually exclusive patterns, separated by vertical bars: ``CM``, ``CD``,and ``D?C?C?C?``. The 
    regular expression parser checks for each of these patterns in order( from left to right), 
    takes the first one that matches, and ignores the rest.

[29]:
    ``'MCM'`` (``1900``) matches because the first ``M`` matches, the second and third ``M`` characters are ignored,
    and the ``CM`` matches (so the ``CD`` and ``D?C?C?C?`` patterns are never considered).

[30]:
    ``'MD'`` (``1500``) matches because the first ``M`` matches, the second and third ``M`` characters are ignored, and the
    ``D?C?C?C?`` pattern matches ``D`` (each of the three ``C`` characters are optional and are ignored).

[31]:
    ``'MMMCCC'"`` (``3300``) matches because all three ``M`` characters match, and the ``D?C?C?C?`` pattern matches ``CCC``.

[33]:
    ``'MCMC'`` does not match. The first ``M`` matches, the second and third ``M`` characters are ignored, and the
    ``'CM'`` matches, but then the ``$`` does not match because you're not at the end of the string yet (you still have
    and unmatched ``C`` character). The ``C`` does *not* match as part of the ``D?C?C?C?`` pattern, because the 
    mutually exclusive ``CM`` pattern has already matched.

7.3.1.2 Using the ``{n.m}`` Syntax
++++++++++++++++++++++++++++++++++

In the previous section, you were dealing with a pattern where the same character could be repeated up to three times.
There is another way to express this in regular expression.

Example 7.5 The New Way: From ``n`` to ``m``

.. admonition:: Key Expression

   ``x{n,m}`` matches an ``x`` character [n,m] times

.. sourcecode:: ipython
   :emphasize-lines: 16

   In [34]: import re

   In [35]: old_pattern = '^M?M?M?M?$'

   In [36]: re.search(old_pattern, 'M')
   Out[36]: <_sre.SRE_Match at 0x92d4528>

   In [37]: re.search(old_pattern, 'MM')
   Out[37]: <_sre.SRE_Match at 0x92d4608>

   In [38]: re.search(old_pattern, 'MMM')
   Out[38]: <_sre.SRE_Match at 0x92d4720>

   In [39]: re.search(old_pattern, 'MMMMM')

   In [40]: new_pattern = '^M{0,4}$'

   In [41]: re.search(new_pattern, 'M')
   Out[41]: <_sre.SRE_Match at 0x92d4988>

   In [42]: re.search(new_pattern, 'MM')
   Out[42]: <_sre.SRE_Match at 0x92d4aa0>

   In [43]: re.search(new_pattern, 'MMM')
   Out[43]: <_sre.SRE_Match at 0x92d4bb8>

   In [44]: re.search(new_pattern, 'MMMMM') 

[40]:
    This patterns says: "Match the start of the string, then anywhere from zero to three ``M`` characters,
    then the end of the string." The ``0`` and ``3`` can be any numbers; if you want to match at least one 
    but no more than three ``M`` characters, you could say ``M{1,3}``.

7.3.1.3 Checking for Tens and Ones
++++++++++++++++++++++++++++++++++
    
 ==================    ====================
   Tens place             Ones place
 ==================    ====================
 ``10`` = ``X``        ``1`` = ``I``
 ``20`` = ``XX``       ``2`` = ``II``
 ``30`` = ``XXX``      ``3`` = ``III``
 ``40`` = ``XL``       ``4`` = ``IV``
 ``50`` = ``L``        ``5`` = ``V``
 ``60`` = ``LX``       ``6`` = ``VI``
 ``70`` = ``LXX``      ``7`` = ``VII``
 ``80`` = ``LXXX``     ``8`` = ``VIII``
 ``90`` = ``XC``       ``9`` = ``IX``
 ==================    ====================

Example 7.6 Checking for Tens

.. sourcecode:: ipython

   In [45]: pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'

   In [46]: re.search(pattern, 'MCMXL')  # 1940
   Out[46]: <_sre.SRE_Match at 0x92440b0>

   In [47]: re.search(pattern, 'MCML') # 1950
   Out[47]: <_sre.SRE_Match at 0x9244e30>

   In [48]: re.search(pattern, 'MCMLX') # 1960
   Out[48]: <_sre.SRE_Match at 0x9244608>

   In [49]: re.search(pattern, 'MCMLXXX') # 1980
   Out[49]: <_sre.SRE_Match at 0x92b1020>
 
   In [50]: re.search(pattern, 'MCMLXXXX') # invalid

7.3.1.4 Final Pattern for Roman Numeral
+++++++++++++++++++++++++++++++++++++++

.. sourcecode:: python
    
    pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

    # using the altenate {n,m} syntax
    alt_pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

.. _verbose_re:

7.4. Verbose Regular Expressions
--------------------------------

.. admonition:: usage

   Writing documentation inside the regular expression.

A *verbose regular expression* is different from a compact regular expression in two ways:

    * Whitespace is ignored. Spaces, tabs, and carriage returns are not matched as spaces, tabs, and carriage returns. 
      They're not matched at all. (If you want to match a space in a verbose regular expression, you'll need to escape it by
      putting a backslash in front of it.)

    * Comments are ignored.

.. sourcecode:: ipython
   :emphasize-lines: 13

   In [51]: pattern = """
       ...:    ^                 # beginning of string
       ...:    M{0,4}            # thousands - 0 to 4 M's
       ...:    (CM|CD|D?C{0,3})  # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
       ...:                      #            or 500-800 (D, followed by 0 to 3 C's)
       ...:    (XC|XL|L?X{0,3})  # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's), 
       ...:                      #        or 50-80 (L, followed by 0 to 3 X's)
       ...:    (IX|IV|V?I{0,3})  # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
       ...:                      #        or 5-8 (V, followed by 0 to 3 I's)
       ...:    $                 # end of string
       ...:    """

   In [52]: re.search(pattern, 'M',re.VERBOSE)
   Out[52]: <_sre.SRE_Match at 0x92d71e0>

   In [53]: re.search(pattern, 'MCMLXXXX', re.VERBOSE)

   In [54]: re.search(pattern, 'MCMLXXXIX', re.VERBOSE)
   Out[54]: <_sre.SRE_Match at 0x9241bb0>

   In [55]: re.search(pattern, 'MMMMDCCCLXXXVIII', re.VERBOSE)
   Out[55]: <_sre.SRE_Match at 0x9241b60>

   In [56]: re.search(pattern, 'M')

[52]:
   The most important thing to remember when using verbose regular expressions is that
   you need to pass an extra argument when working with them: ``re.VERBOSE`` is a 
   constant defined in the ``re`` module that signals that the pattern should be treated
   as a verbose regular expression.

[56]:
    ``re.VERBOSE`` flag is missing. Python assumes every regular expression is compact unless
    you explicitly state that it is verbose.


.. _case_stuy_phone:

7.5. Case Study: Parsing Phone Numbers
--------------------------------------

When a regular expression *does* match, you can pick out specific pieces of it. You can find out what matched where.

The problem:

    parsing an American phone number. The client wanted to be able to enter the number free-form (in a single field), 
    but then wanted to store the area code, trunk, number, and optionally an extension separately in the company's database.

Here are the possible forms of phone numbers:

    * 800-555-1212
    * 800 555 1212
    * 800.555.1212
    * (800) 555-1212
    * 1-800-555-1212
    * 800-555-1212-1234
    * 800-555-1212x1234
    * 800-555-1212 ext. 1234
    * work 1-(800) 555.1212 #1234

In each of these case, I need to know that the area code was ``800``, the trunk was ``555``, and the rest of the phone number was ``1212``.
For those with an extension, I need to know that the extension was ``1234``.

Example 7.10 Finding Numbers

.. admonition:: Key Expression

   ``\d`` means "any numeric digit" (0 through 9).

.. admonition:: Key Func

   patternObj = re.compile(pattern)
   
   patternObj.search(string).groups()

.. sourcecode:: ipython
   :emphasize-lines: 3,8
   
   In [1]: import re

   In [2]: phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

   In [3]: type(phonePattern)
   Out[3]: _sre.SRE_Pattern

   In [4]: phonePattern.search('800-555-1212').groups()
   Out[4]: ('800', '555', '1212')

   In [5]: phonePattern.search('800-555-1212-1234')

[2]:
    * re.complie::

        # compile a regular expression pattern into a regular expression object,
        # which can be used for matching using its match() and search() methods
        patternObj = re.compile(pattern)

    * ``\d``:
        
        - ``{3}`` means "match exactly three numeric digits" (a variation on the ``{n,m} syntax``)
        - ``\d`` means "any numeric digit" (0 through 9)
        - ``(\d{3})`` means "match exactly three numeric digits, and *then remember them as a group that I can ask for later*"

[4]:
    * groups()::
        
        # to get access to the groups that the regular expression parser remembered along the way
        # it will return a tuple of however many groups were defined in the regular expression.
        patternObj.search(string).groups()

    * In this case, you defined three groups, one with three digits, one with three digits, and one with four digits.

[5]:
    .. admonition:: problem

       This regular expression doesn't handle a phone number with an extension on the end.

Example 7.11 Finding the Extension

.. admonition:: Key Expression

   ``x+`` matches ``x`` one or more times

.. sourcecode:: ipython
   :emphasize-lines: 6
   
   In [6]: phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')

   In [7]: phonePattern.search('800-555-1212-1234').groups()
   Out[7]: ('800', '555', '1212', '1234')

   In [8]: phonePattern.search('800 555 1212 1234')

   In [9]: phonePattern.search('800-555-1212')

[6]:
    * ``\d+``:

        - ``x+`` matches ``x`` one or more times.

        - ``\d+`` means "match one or more numeric digits"

    * This regular expression is almost identical to the previous one: 
      you match the beginning of the string, then a remembered group of three digits,
      then a hyphen, then a remembered group of three digits, then a hyphen, then 
      a remembered group of four digits,then match another hyphen, and 
      a remembered group of one or more digits, then the end of the string.

[8]&[9]:
    .. admonition:: problem

       * it assumes that the different parts of the phone number are separated by hyphens.
         What if they're separated by spaces, or commas, or dots?

       * You cannot parse phone numbers without and extension.

Example 7.12 Handling Different Separators

.. admonition:: Key Expression

   ``\D`` matches any non-numeric character.

.. sourcecode:: ipython
   :emphasize-lines: 1

   In [10]: phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')

   In [11]: phonePattern.search('800 555 1212 1234').groups()
   Out[11]: ('800', '555', '1212', '1234')

   In [12]: phonePattern.search('800-555-1212-1234').groups()
   Out[12]: ('800', '555', '1212', '1234')

   In [13]: phonePattern.search('8005551212')

   In [14]: phonePattern.search('800-555-1212')
   
[10]:
    ``\D``:
        
        - ``\D`` matches any character *except* a numeric digit.

        - ``\D+`` matchs one or more characters that are not digits. (this is how you try to match different separators)

[13]&[14]:
    .. admonition:: problem

       * it assumes that there is a separator at all. What if the phone number is entered without any spaces or hyphens?

       * extensions are still required.

Example 7.13 Handling Numbers Without Separators

.. admonition:: Key Expression

   ``x*`` matches ``x`` zero or more times.

.. sourcecode:: ipython
   :emphasize-lines: 1

   In [15]: phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

   In [16]: phonePattern.search('80055512121234').groups()
   Out[16]: ('800', '555', '1212', '1234')

   In [18]: phonePattern.search('800.555.1212 x1234').groups()
   Out[18]: ('800', '555', '1212', '1234')

   In [21]: phonePattern.search('800-555-1212').groups()
   Out[21]: ('800', '555', '1212', '')

   In [22]: phonePattern.search('(800)5551212 x1234')

[15]:
    ``*``:

        - ``X*`` matches ``x`` zero or more times.

        - The only change you've made since that last step is changing all the ``+`` to ``*``.
          Instead of ``\D+`` between the parts of the phone number, you now match on ``\D*``.
          It means "match non-numeric character(s) zero or more times".

[22]:
    .. admonition:: problem

       There's an extra character before the area code, but the regular expression assumes that the
       area code is the first thing at the beginning of the string.

Example 7.14 Handling Leading Characters

.. sourcecode:: ipython
   :emphasize-lines: 1

   In [23]: phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

   In [24]: phonePattern.search('(800)5551212 ext. 1234').groups()
   Out[24]: ('800', '555', '1212', '1234')

   In [25]: phonePattern.search('800-555-1212').groups()
   Out[25]: ('800', '555', '1212', '')

   In [26]: phonePattern.search('work 1-(800) 555.1212 #1234').groups()
   Out[26]: ('800', '555', '1212', '1234')

[23]:
    Note the lack of ``^`` in this regular expression.
    You are not matching the beginning of the string anymore.

Example 7.15 Parsing Phone Numbers (Final Version)

.. sourcecode:: ipython

   In [27]: phonePattern = re.compile(r'''
       ...:              # don't match beginning of string, number can start anywhere
       ...: (\d{3})      # area code is 3 digits (e.g. '800')
       ...: \D*          # optional separator is any number of non-digits
       ...: (\d{3})      # trunk is 3 digits (e.g. '555')
       ...: \D*          # optional separator
       ...: (\d{4})      # rest of number is 4 digits (e.g. '1212')
       ...: \D*          # optional separator
       ...: (\d*)        # extension is optional and can be any number of digits
       ...: $            # end of string
       ...: ''', re.VERBOSE)

   In [28]: phonePattern.search('work 1-(800) 555.1212 #1234').groups()
   Out[28]: ('800', '555', '1212', '1234')

   In [29]: phonePattern.search('800-555-1212').groups()
   Out[29]: ('800', '555', '1212', '') 


.. _further_reading7:

7.6. Further Reading
--------------------

* Regular Expression `HOWTO`__ teaches about regular expressions and how to use them in Python.

* `re`_ module

__ regex_

























.. include:: ../../../links.rst
