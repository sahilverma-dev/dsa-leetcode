# Question 2: Group Anagrams
# Problem Statement:
# Given an array of strings, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    dict = {}

    for i in strs:
        joined = "".join(sorted(i))
        if joined in dict:
            dict[joined].append(i)
        else:
            dict[joined] = [i]

    return list(dict.values())


# Example:
print(
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(group_anagrams([""]))  # Output: [[""]]
print(group_anagrams(["a"]))  # Output: [["a"]]
