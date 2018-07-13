import re

def decode(string):
    return string


def encode(string):
    retval        = '';
    current_count = 0;
    current_char  = '';
    total_count   = 1;

    for l in string:
        at_end = total_count == len(string)

        if (not l == current_char and current_count > 0) or (at_end):
            # Bump one more if we're all the way at the end, actually.
            if (True == at_end):
                current_count += 1

            retval += '{0}{1}'.format(current_count, current_char)
            current_count = 0;

        current_count += 1
        total_count   += 1
        current_char   = l

    return retval
