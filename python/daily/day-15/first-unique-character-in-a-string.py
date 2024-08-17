# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# 387. First Unique Character in a String
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.


from collections import Counter, deque


def firstUniqChar(s: str) -> int:
    # queue = []
    # hash_map = {}

    # for char in s:
    #     if char in hash_map:
    #         hash_map[char] += 1
    #     else:
    #         hash_map[char] = 1

    # print(hash_map)

    # for char in s:
    #     if hash_map[char] == 1:
    #         queue.append(char)

    # if queue:
    #     return s.index(queue[0])
    # else:
    #     return -1

    char_count = [0] * 26
    for char in s:
        char_count[ord(char) - ord("a")] += 1
    for i, char in enumerate(s):
        if char_count[ord(char) - ord("a")] == 1:
            return i
    return -1

    # freq = {}
    # q = deque()

    # for i, ch in enumerate(s):
    #     if ch in freq:
    #         freq[ch] += 1
    #     else:
    #         freq[ch] = 1
    #     q.append((ch, i))

    # print(freq, q)

    # while q:
    #     ch, idx = q[0]
    #     if freq[ch] == 1:
    #         return idx
    #     else:
    #         q.popleft()

    # return -1


# Example 1:
# Input: s = "leetcode"
# Output: 0
print("Example 1:", firstUniqChar("leetcode"))  # 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# print("Example 2:", firstUniqChar("loveleetcode"))  # 2

# Example 3:
# Input: s = "aabb"
# Output: -1
# print("Example 3:", firstUniqChar("aabb"))  # -1
# print("Example 4:", firstUniqChar("adaccdcda"))  # -1


# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
