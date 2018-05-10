def is_isogram(string):
    word_list = list(string)
    test_list = list()
    sempaphor = True

    for w in word_list:
        if (False == w.isalpha()):
            continue

        if (w in test_list):
            sempaphor = False

        test_list.append(w.lower())

    return sempaphor
