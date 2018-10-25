"""
The isogram exercise on the python track in exercism.io
"""


def is_isogram(string):
    """
    Given a string, determines if it is an isogram,
    that is - does it have the same letter in it twice?
    """
    word_list = list(string)
    test_list = list()
    semaphor = True

    for _ in word_list:
        if not _.isalpha():
            continue

        if _.lower() in test_list:
            semaphor = False

        test_list.append(_.lower())

    return semaphor
