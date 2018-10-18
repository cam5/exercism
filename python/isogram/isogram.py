def is_isogram(string):
    word_list = list(string)
    test_list = list()
    semaphor = True

    for w in word_list:
        if (False == w.isalpha()):
            continue

        if (w in test_list):
            semaphor = False

        test_list.append(w.lower())

    return semaphor
