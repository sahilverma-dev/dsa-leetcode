def maxScore(s: str) -> int:

    # brute force
    # max_score = 0
    # n = len(s)

    # for i in range(1, n):
    #     left = s[:i]
    #     right = s[i:]

    #     score = left.count("0") + right.count("1")

    #     max_score = max(max_score, score)

    # return max_score

    # prefix sum
    zeros = 0
    ones = s.count("1")
    ans = 0

    for i in range(len(s) - 1):
        if s[i] == "0":
            zeros += 1
        else:
            ones -= 1
        ans = max(ans, zeros + ones)

    return ans


print("Example 1:", maxScore("011101"))  # 5
print("Example 2:", maxScore("00111"))  # 5
print("Example 3:", maxScore("1111"))  # 3
