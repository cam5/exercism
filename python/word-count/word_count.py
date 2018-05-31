import re

def word_count(phrase):
    words = {}

    # Internal counting func.
    def word_counter(w):
        if words.get(w) == None:
            words[w] = 0

        words[w] = words[w] + 1


    """Catch only word characters,
    but allow for a single quote in the middle, in consideration of
    contractions. Note: this would names with multiple ' characters.

    The 'r' at the start of the pattern string designates a python "raw"
    string which passes through backslashes without change which is very handy
    for regular expressions. [We] recommend that you always write pattern strings
    with the 'r' just as a habit.
    """
    exploded_words = re.split(r'\b([\w|\']+)\b', phrase)

    words_from_phrase = [str(w).lower() for w in exploded_words if re.match(r'\w+', w)]

    for w in words_from_phrase:
        # If there are underscores, break that up, too.
        if '_' in w:
            for w in w.split('_'):
                word_counter(w)
        # Else total like normal
        else:
            word_counter(w)

    return words
