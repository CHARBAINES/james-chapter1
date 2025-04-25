# james-chapter1-python
This is a Python program for looking up a Bible verse and viewing three versions of the verse at the same time for comparison and study.
For this test program I used the first chapter of the New Testament book of James. The text is from the following versions:
King James Version, New International Version, and Revised Standard Version

The main program is:
james_chapter1_lookup.py

The Bible verse data can be found in these files:
kjv_james_chapter1.py
niv_james_chapter1.py
rsv_james_chapter1.py

The lookup functions are in this file:
scripture_lookup.py


This project gave me the opportunity to work with python dicts, functions, modules, and exceptions. 

I stored the Bible verses in dictionaries where the verse numbers were the dictionary keys, and the Bible verses were the dictionary values.
I created a function called get_verse() to print the Bible verse while handling exceptions for:
1) KeyErrors -  if the number provided by the user was not found in the dictionary key set,
2) ValUeErrors - if something other than an integer was input by the user.

I then created a function called bible_multiverse() that requests integer input from a user.
This input is then passed to the get_verse() function 3 times, once for each version of the scripture.
This function also handles KeyErrors and ValueErrors the same as get_verse().
