# 2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.

# Return an array of indices representing the words that contain the character x.

# Note that the returned array may be in any order.

from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    # brute force
    ans = []
    for i, word in enumerate(words):
        if x in word:
            ans.append(i)
    return ans


# Example 1:

# Input: words = ["leet","code"], x = "e"
print(findWordsContaining(words=["leet", "code"], x="e"))  # Output: [0,1]
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
# Example 2:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="a"))  # Output: [0,2]
# Output: [0,2]
# Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
# Example 3:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="z"))  # Output: []
# Output: []
# Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
