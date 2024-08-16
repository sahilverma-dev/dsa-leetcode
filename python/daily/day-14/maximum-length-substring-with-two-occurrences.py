# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

# 3090. Maximum Length Substring With Two Occurrences
# Easy
# Topics
# Companies
# Hint
# Given a string s, return the maximum length of a
# substring
#  such that it contains at most two occurrences of each character.


# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


def maximumLengthSubstring(s: str) -> int:
    #  brute force
    max_num = 0
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_str = s[i:j]

            count = {}
            is_valid = True

            for char in sub_str:
                if char in count:
                    count[char] += 1

                    if count[char] > 2:
                        is_valid = False
                        break
                else:
                    count[char] = 1
            if is_valid:
                max_num = max(max_num, len(sub_str))

    return max_num


# Example usage
print(maximumLengthSubstring("bcbbbcba"))  # Output: 4
print(maximumLengthSubstring("aaaa"))  # Output: 2
