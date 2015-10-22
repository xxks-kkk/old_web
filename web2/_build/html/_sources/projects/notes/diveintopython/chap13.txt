.. _chap13:

============
Unit Testing
============

In the next few chapters, you're going to write, debug, and optimize a set of utility functions
to convert to and from Roman numerals.

.. _intro_to_roman_numerals:

13.1 Introduction to Roman numerals
-----------------------------------

13.1.0 Basic Rules in Roman numerals
************************************

see :ref:`Case Study: Roman numerals <case_study_roman>` in Section 7.3 

13.1.1 Observations
*******************

The rules for Roman numerals lead to a number of interesting observations:

    1. There is only one correct way to represent a particular number as Roman numerals.
    2. The converse is also true: if a string of characters is a valid Roman numeral, it represents only one number
       (*i.e.* it can only be read one way).
    3. There is a limited range of numbers that can be expressed as Roman numerals, specifically ``1`` through ``3999``. [#]_ [#]_
    4. There is no way to represent 0 in Roman numerals.
    5. There is no way to represent negative numbers in Roman numerals.
    6. There is no way to represent fractions or non-integer numbers in Roman numerals. [#]_

.. _intro_to_unit_testing:

13.2 Introduction to Unit Testing
---------------------------------

Unit Testing:
    1. basic idea: 
        
        you're going to write a test suite that puts these functions through their paces and makes
        sure that they behave the way you want them to.
        (In other words, you're going to write code that tests code that you haven't written yet.)

    2. what's "Unit"?
        
        Since the set of two conversion functions can be written and tested as a unit,
        separate from any larger program they may become part of later.

    3. Why it's important?
        
        If you write unit tests, it is important to write them early (perferably before writing the
        code that they test), and to keep them updated as code and requirements change.

        Unit testing is not a replacement for higher-level functional or system testing, but it
        is important in all phases of development:

            * Before writing code, it forces you to detail your requirements in a useful fashion.
            * While writing code, it keeps you from over-coding. When all the test cases pass, the function is complete.
            * When refactoring code, it assures you that the new version behaves the same way as the old version.

    4. How to do it in Python?
        
        Python has a framework for unit testing, the appropriately-named `unittest`_ module. There is another detailed `introduction`__
        about this framework.

__ unittest_frame_


.. _romantest.py:

13.3 Introducing ``romantest.py``
---------------------------------

Given the rules and observations in Roman numerals, what would you expect out of a set of functions to convert to and
from Roman numerals?

``roman.py`` requirements
    1. ``toRoman`` should return the Roman numeral representation for all integers ``1`` to ``3999``.
    2. ``toRoman`` should fail when given an integer outside the range ``1`` to ``3999``.
    3. ``toRoman`` should fail when given a non-integer number.
    4. ``fromRoman`` should take a valid Roman numeral and return the number that it represents.
    5. ``fromRoman`` should fail when given an invalid Roman numeral.
    6. If you take a number, convert it to Roman numerals, then convert that back to a number, you
       should end up with the number you started with. So ``fromRoman(toRoman(n)) == n`` for all
       ``n`` in ``1 ... 3999``.
    7. ``toRoman`` should always return a Roman numeral using uppercase letters.
    8. ``fromRoman`` should only accept uppercase Roman numerals (*i.e.* it should fail when given lowercase input).

Then, the ``romantest.py`` should be a complete test suite to see whether the Roman numeral conversion functions meet
those requirements.

Example 13.1 romantest.py (download `here <../../../_static/projects/notes/diveintopython/py/romantest.py>`_)

.. sourcecode:: python
   :linenos:

   import roman
   import unittest

   class KnownValues(unittest.TestCase):
	   knownValues = ( (1, 'I'),
			   (2, 'II'),
			   (3, 'III'),
			   (4, 'IV'),
			   (5, 'V'),
			   (6, 'VI'),
			   (7, 'VII'),
			   (8, 'VIII'),
			   (9, 'IX'),
			   (10, 'X'),
			   (50, 'L'),
			   (100, 'C'),
			   (500, 'D'),
			   (1000, 'M'),
			   (31, 'XXXI'),
			   (148, 'CXLVIII'),
			   (294, 'CCXCIV'),
			   (312, 'CCCXII'),
			   (421, 'CDXXI'),
			   (528, 'DXXVIII'),
			   (621, 'DCXXI'),
			   (782, 'DCCLXXXII'),
			   (870, 'DCCCLXX'),
			   (941, 'CMXLI'),
			   (1043, 'MXLIII'),
			   (1110, 'MCX'),
			   (1226, 'MCCXXVI'),
			   (1301, 'MCCCI'),
			   (1485, 'MCDLXXXV'),
			   (1509, 'MDIX'),
			   (1607, 'MDCVII'),
			   (1754, 'MDCCLIV'),
			   (1832, 'MDCCCXXXII'),
			   (1993, 'MCMXCIII'),
			   (2074, 'MMLXXIV'),
			   (2152, 'MMCLII'),
			   (2212, 'MMCCXII'),
			   (2343, 'MMCCCXLIII'),
			   (2499, 'MMCDXCIX'),
			   (2574, 'MMDLXXIV'),
			   (2646, 'MMDCXLVI'),
			   (2723, 'MMDCCXXIII'),
			   (2892, 'MMDCCCXCII'),
			   (2975, 'MMCMLXXV'),
			   (3051, 'MMMLI'),
			   (3185, 'MMMCLXXXV'),
			   (3250, 'MMMCCL'),
			   (3313, 'MMMCCCXIII'),
			   (3408, 'MMMCDVIII'),
			   (3501, 'MMMDI'),
			   (3610, 'MMMDCX'),
			   (3743, 'MMMDCCXLIII'),
			   (3844, 'MMMDCCCXLIV'),
			   (3888, 'MMMDCCCLXXXVIII'),
			   (3940, 'MMMCMXL'),
			   (3999, 'MMMCMXCIX'),
			   (4000, 'MMMM'),
			   (4500, 'MMMMD'),
			   (4888, 'MMMMDCCCLXXXVIII'),
			   (4999, 'MMMMCMXCIX'))

	   def testToRomanKnownValues(self):
		   """toRoman should give known result with known input"""
		   for integer, numeral in self.knownValues:
			   result = roman.toRoman(integer)
			   self.assertEqual(numeral, result)

	   def testFromRomanKnownValues(self):
		   """fromRoman should give known result with known input"""
		   for integer, numeral in self.knownValues:
			   result = roman.fromRoman(numeral)
			   self.assertEqual(integer, result)

   class ToRomanBadInput(unittest.TestCase):
	   def testTooLarge(self):
		   """toRoman should fail with large input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, 5000)

	   def testZero(self):
		   """toRoman should fail with 0 input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

	   def testNegative(self):
		   """toRoman should fail with negative input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

	   def testDecimal(self):
		   """toRoman should fail with non-integer input"""
		   self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)

   class FromRomanBadInput(unittest.TestCase):
	   def testTooManyRepeatedNumerals(self):
		   """fromRoman should fail with too many repeated numerals"""
		   for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	   def testRepeatedPairs(self):
		   """fromRoman should fail with repeated pairs of numerals"""
		   for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	   def testMalformedAntecedent(self):
		   """fromRoman should fail with malformed antecedents"""
		   for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
				   'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	   def testBlank(self):
		   """fromRoman should fail with blank string"""
		   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, "")

   class SanityCheck(unittest.TestCase):
	   def testSanity(self):
		   """fromRoman(toRoman(n))==n for all n"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   result = roman.fromRoman(numeral)
			   self.assertEqual(integer, result)

   class CaseCheck(unittest.TestCase):
	   def testToRomanCase(self):
		   """toRoman should always return uppercase"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   self.assertEqual(numeral, numeral.upper())

	   def testFromRomanCase(self):
		   """fromRoman should only accept uppercase input"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   roman.fromRoman(numeral.upper())
			   self.assertRaises(roman.InvalidRomanNumeralError,roman.fromRoman, numeral.lower())

   if __name__ == "__main__":
	   unittest.main() 

.. _testing_for_success:

13.4 Testing for success
------------------------

The most fundamental part of unit testing is constructing **individual test cases**.
A test case answers a *single* question about the code it is testing.

A test case should be able to:
    * run completely by itself, without any human input. Unit testing is about automation.
    * determine by itself whether the function it is testing has passed or failed,
      without a human interpreting the results.
    * run in isolation, separate from any other test cases (even if they test the same functions).
      Each test case is an island.


Example 13.2 testToRomanKnownValues

Test:
    1. ``toRoman`` should return the Roman numeral representation for all integers ``1`` to ``3999``.

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 1,63,67

      class KnownValues(unittest.TestCase):
	   knownValues = ( (1, 'I'),
			   (2, 'II'),
			   (3, 'III'),
			   (4, 'IV'),
			   (5, 'V'),
			   (6, 'VI'),
			   (7, 'VII'),
			   (8, 'VIII'),
			   (9, 'IX'),
			   (10, 'X'),
			   (50, 'L'),
			   (100, 'C'),
			   (500, 'D'),
			   (1000, 'M'),
			   (31, 'XXXI'),
			   (148, 'CXLVIII'),
			   (294, 'CCXCIV'),
			   (312, 'CCCXII'),
			   (421, 'CDXXI'),
			   (528, 'DXXVIII'),
			   (621, 'DCXXI'),
			   (782, 'DCCLXXXII'),
			   (870, 'DCCCLXX'),
			   (941, 'CMXLI'),
			   (1043, 'MXLIII'),
			   (1110, 'MCX'),
			   (1226, 'MCCXXVI'),
			   (1301, 'MCCCI'),
			   (1485, 'MCDLXXXV'),
			   (1509, 'MDIX'),
			   (1607, 'MDCVII'),
			   (1754, 'MDCCLIV'),
			   (1832, 'MDCCCXXXII'),
			   (1993, 'MCMXCIII'),
			   (2074, 'MMLXXIV'),
			   (2152, 'MMCLII'),
			   (2212, 'MMCCXII'),
			   (2343, 'MMCCCXLIII'),
			   (2499, 'MMCDXCIX'),
			   (2574, 'MMDLXXIV'),
			   (2646, 'MMDCXLVI'),
			   (2723, 'MMDCCXXIII'),
			   (2892, 'MMDCCCXCII'),
			   (2975, 'MMCMLXXV'),
			   (3051, 'MMMLI'),
			   (3185, 'MMMCLXXXV'),
			   (3250, 'MMMCCL'),
			   (3313, 'MMMCCCXIII'),
			   (3408, 'MMMCDVIII'),
			   (3501, 'MMMDI'),
			   (3610, 'MMMDCX'),
			   (3743, 'MMMDCCXLIII'),
			   (3844, 'MMMDCCCXLIV'),
			   (3888, 'MMMDCCCLXXXVIII'),
			   (3940, 'MMMCMXL'),
			   (3999, 'MMMCMXCIX'),
			   (4000, 'MMMM'),
			   (4500, 'MMMMD'),
			   (4888, 'MMMMDCCCLXXXVIII'),
			   (4999, 'MMMMCMXCIX'))

	   def testToRomanKnownValues(self):
		   """toRoman should give known result with known input"""
		   for integer, numeral in self.knownValues:
			   result = roman.toRoman(integer)
			   self.assertEqual(numeral, result)

[1]:
    To write a test case, first subclass the ``Testcase`` class of the ``unittest`` module.
    This class provides many useful methods which you can use in your test case to test specific conditions.
   
[2]:
    This is a list of integer/numeral pairs that I verified manually. It includes the lowest ten numbers, the 
    highest number, every number that translates to a single-character Roman numeral, and a random sampling
    of other valid numbers. The point of a unit test is not to test every possible input, but to test a 
    representative sample.

[63]:
    Every individual test is its own method, which must take no parameters and return no value.
    If the method exits normally without raising an exception, the test is considered passed;
    if the method raises an exception, the test is considered failed.

[66]:
    * Here you call the actual ``toRoman`` function. 
      Notice that you have now defined the API for the ``toRoman`` function: 
      it must take an integer (the number to convert) and return a string (the Roman numeral representation).
      If the API is different than that, this test is considered failed.

    * Also notice that you are not trapping any exceptions when you call ``toRoman``. This is intentional.
      ``toRoman`` shouldn't raise an exception when you call it with valid input, and these input values are
      all valid. If ``toRoman`` raises an exception, this test is considered failed.

[67]:
    To check whether ``toRoman`` returned the *right* value.
    The ``TestCase`` class provides a method, ``assertEqual``, to check whether two values are equal.
    If the result returned from ``toRoman`` (*result*) does not match the known value you were expecting (*numeral*),
    ``assertEqual`` will raise an exception and the test will fail. If the two values are equal, ``assertEqual`` will
    do nothing. If every value returned from ``toRoman`` matches the known value you expect, ``assertEqual`` never
    raises an exception, so ``testToRomanKnownValues`` eventually exits normally, which means ``toRoman`` has passed this
    test.


.. _testing_for_failure:

13.5 Testing for failure
-------------------------

Example 13.3 Testing bad input to toRoman

Test:
    2. ``toRoman`` should fail when given an integer outside the range ``1`` to ``3999``.
    3. ``toRoman`` should fail when given a non-integer number.

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 4

   class ToRomanBadInput(unittest.TestCase):
	   def testTooLarge(self):
		   """toRoman should fail with large input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, 5000)

	   def testZero(self):
		   """toRoman should fail with 0 input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

	   def testNegative(self):
		   """toRoman should fail with negative input"""
		   self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

	   def testDecimal(self):
		   """toRoman should fail with non-integer input"""
		   self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)

[4]:
    * The ``TestCase`` class of the ``unittest`` provides the ``assertRaises`` method,
      which takes the following arguments: 
        
        - the exception you're expecting
        - the function you're testing
        - the arguments you're passing that function (if the function you're testing 
          takes more than one argument, pass them all to ``assertRaises``, in order,
          and it will pass them right along to the function you're testing.)
 
    * Here, instead of calling ``toRoman`` directly and manually checking that it raises
      a particular exception (by wrapping it in a ``try ... except`` block),
      ``assertRaises`` has encapsulated all of that for us. 
      All you do is give it the exception (``roman.OutOfRangeError``), the function (``toRoman``),
      and ``toRoman``'s arguments (``4000``), and ``assertRaises`` takes care of calling ``toRoman``
      and checking to make sure that it raises ``roman.OutOfRangeError``.

Example 13.4 Testing bad input to fromRoman

Test:
    4. ``fromRoman`` should take a valid Roman numeral and return the number that it represents.
    5. ``fromRoman`` should fail when given an invalid Roman numeral.

.. sourcecode:: python
   :linenos:

   class FromRomanBadInput(unittest.TestCase):
	   def testTooManyRepeatedNumerals(self):
		   """fromRoman should fail with too many repeated numerals"""
		   for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	   def testRepeatedPairs(self):
		   """fromRoman should fail with repeated pairs of numerals"""
		   for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	   def testMalformedAntecedent(self):
		   """fromRoman should fail with malformed antecedents"""
		   for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
				   'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
			   self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)   

.. _testing_for_sanity:

13.6 Testing for Sanity
-----------------------

Often, you will find that a unit of code contains a set of reciprocal functions, usually
in the form of conversion functions where one converts A to B and the other converts
B to A. In these cases, it is useful to create a "sanity check" to make sure that you 
can convert A to B and back to A without losing precision, incurring rounding errors,
or triggering any other sort of bug.

Example 13.5 Testing toRoman against fromRoman

Test:
    6. If you take a number, convert it to Roman numerals, then convert that back to a number, you
       should end up with the number you started with. So ``fromRoman(toRoman(n)) == n`` for all
       ``n`` in ``1 ... 3999``.

.. sourcecode:: python
   :linenos:
   
   class SanityCheck(unittest.TestCase):
       def testSanity(self):
		   """fromRoman(toRoman(n))==n for all n"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   result = roman.fromRoman(numeral)
			   self.assertEqual(integer, result)

Example 13.6 Testing for Case

Test:
    7. ``toRoman`` should always return a Roman numeral using uppercase letters.
    8. ``fromRoman`` should only accept uppercase Roman numerals (*i.e.* it should fail when given lowercase input).

.. sourcecode:: python
   :linenos:
   :emphasize-lines: 6,12

   class CaseCheck(unittest.TestCase):
	   def testToRomanCase(self):
		   """toRoman should always return uppercase"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   self.assertEqual(numeral, numeral.upper())

	   def testFromRomanCase(self):
		   """fromRoman should only accept uppercase input"""
		   for integer in range(1, 5000):
			   numeral = roman.toRoman(integer)
			   roman.fromRoman(numeral.upper())
			   self.assertRaises(roman.InvalidRomanNumeralError,roman.fromRoman, numeral.lower())
 
[6]:
   The most interesting thing about this test case is all the things it doesn't test. It doesn't
   test that the value returned from ``toRoman`` is right or even consisten; those questions
   are answered by separate test cases. You have a whole test case just to test for uppercase-ness.
   You might be tempted to combine this with the sanity check, since both run through the entire
   range of values and call ``toRoman``. But that would violate one of the fundamental rules:
   
   each test case should answer only a single question:
            Imagine that you combined this case check with the sanity check, and then that test case failed.
            You would need to do further analysis to figure out which part of the test case failed to determine
            what the problem was. If you need to analyze the results of your unit testing just to figure out
            what they mean, it's a sure sign that you've mis-designed your test cases.

[12]:
    There's a similar lesson to be learned here: even though "you know" that ``toRoman`` always returns uppercase.
    you are explicitly converting its return value to uppercase here to test that ``fromRoman`` accepts uppercase input.
    
    reason:

        ``toRoman`` always returns uppercase is an independent requirement. If you changed that requirement so that, for
        instance, it always returned lowercase, the ``testToRomanCase`` test case would need to change, but this test Case
        would still work. This was another of the fundamental rules: **each test case must be able to work in isolation from
        any of the others. Every test case is an island.**






































































































**Footnotes**

.. [#] The Romans did have several ways of expressing larger numbers, for instance by having a bar over a numeral to represent that its normal value
       should be multiplied by 1000, but you're not going to deal with that. For the purposes of this chapter, let's stipulate that Roman numerals go
       from 1 to 3999.

.. [#] Whether to 3999 or to 4999 is argurable. This simply because whether it is correct to represent 4000 with "MMMM". If this is not true, then
       the limit should be 3999. Otherwise, it should be 4999.

.. [#] Actually, there is. See `here <http://en.wikipedia.org/wiki/Roman_numerals#Fractions>`_


.. include:: ../../../links.rst
