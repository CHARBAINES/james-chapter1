# scripture_lookup.py -- lookup functions

from kjv_james_chapter1 import *
from niv_james_chapter1 import *
from rsv_james_chapter1 import *

def get_verse(chapter, verse):
    """Selecting a Bible verse to display."""
    print()
    try:
        print(chapter[verse])
    except KeyError:
        print("That verse does not exist.")  
    except ValueError:
        print("That is not a valid entry.")


def bible_multiverse():
    """Returns three versions of a Bible verse."""
    try:
        verse = int(input("\nEnter a verse number: "))
        print('\nKing James Version')
        get_verse(kjv_james_chapter1, verse)
        print('...............................................................' \
        '.....')
        print('\nNew International Version')
        get_verse(niv_james_chapter1, verse)
        print('...............................................................' \
        '.....')
        print('\nRevised Standard Version')
        get_verse(rsv_james_chapter1, verse)
        print('...............................................................' \
        '.....')   
    except KeyError:
        print("That verse does not exist.")  
    except ValueError:
        print("That is not a valid entry.")
    bible_multiverse()