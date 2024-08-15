def isAnagram(s, t):
    dict = {}

    if len(s) != len(t):
        return False

    for c1 in s:
        if c1 in dict:
            dict[c1] += 1
        else:
            dict[c1] = 1

    for c2 in t:
        if c2 in dict:
            dict[c2] -= 1
        else:
            dict[c2] = -1

    return all(value == 0 for value in dict.values())


print(isAnagram(s="anagram", t="nagaram"))
