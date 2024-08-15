def count_in_sentence(sentence):
    vowel_count = 0
    consonant_count = 0

    vowels = ["a", "e", "i", "o", "u"]
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for c in sentence:
        if c in vowels:
            vowel_count += 1
        if c in consonants:
            consonant_count += 1

    print("consonants: ", consonant_count)
    print("vowel: ", vowel_count)


count_in_sentence("abcde")
