import re

def decode(string):
    return string


def encode(string):
    retval            = '';
    current_run_count = 0;
    current_run_char  = '';

    for l in string:
        if not l == current_run_char:
            current_run_count = 1
        else:
            current_run_count += 1

        current_run_char = l

        retval += '{0}{1}'.format(current_run_count, current_run_char)

        print(l, current_run_count, current_run_char)

    return retval
