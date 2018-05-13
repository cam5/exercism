import string

def is_pangram(sentence):
    sentence_letters = list(sentence.lower())
    alphabet_letters = list(string.ascii_lowercase)

    for l in sentence_letters:
        if (l in alphabet_letters and l in alphabet_letters):
            alphabet_letters.remove(l)

    return 0 == len(alphabet_letters)
