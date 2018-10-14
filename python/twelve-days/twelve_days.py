"""12 Days of Christmas exercise from exercism.io"""

BASE = "On the {} day of Christmas "
VERSES = ["twelve Drummers Drumming, ",
          "eleven Pipers Piping, ",
          "ten Lords-a-Leaping, ",
          "nine Ladies Dancing, ",
          "eight Maids-a-Milking, ",
          "seven Swans-a-Swimming, ",
          "six Geese-a-Laying, ",
          "five Gold Rings, ",
          "four Calling Birds, ",
          "three French Hens, ",
          "two Turtle Doves, ",
          "and a Partridge in a Pear Tree."]


def num_to_suffixed_text(num):
    """Just a little lookup"""
    return ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
            'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][num - 1]

def get_verse(num):
    output = []

    output.append(BASE.format(num_to_suffixed_text(num)))
    output.append("my true love gave to me, ")

    if num == 1:
        output.append('a Partridge in a Pear Tree.')
    else:
        for gift in range(num * -1, 0):
            """
            Second arg of range, `stop`, is "up to, but not including"
            Therefore, if we access VERSES backwards (with -n notation),
            stopping at -1 (the last element, then we get our verse.)
            """
            output.append(VERSES[gift])

    return ''.join(output)


def recite(start_verse, end_verse):
    """Recite the day of christmas, given a start and end verse."""
    verses = []

    if start_verse == end_verse:
        verses.append(get_verse(start_verse))

    for verse in range(start_verse, end_verse):
        verses.append(get_verse(verse))

    return verses
