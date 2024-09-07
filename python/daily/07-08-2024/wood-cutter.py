# https://www.hackerearth.com/problem/algorithm/woodcutter/


# Chotu needs to chop down M metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. However, Chotu is only allowed to cut a single row of trees.
# Chotu's machine works as follows: Chotu sets a height parameter H (in metres), and the machine raises a giant sawblade to that height and cuts off all tree parts higher than H (of course, trees not higher than H meters remain intact). Chotu then takes the parts that were cut off.
# For example, if the tree row contains trees with heights of 20, 15, 10, and 17 metres, and Chotu raises his sawblade to 15 metres, the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, respectively, while Chotu will take 5 metres off the first tree and 2 metres off the fourth tree (7 metres of wood in total).
# Chotu is ecologically minded, so he doesn‟t want to cut off more wood than necessary. That‟s why he wants to set his sawblade as high as possible. Help Chotu find the maximum integer height of the sawblade that still allows him to cut off at least M metres of wood.

# Input
# First line of input contains integer N (number of trees) and M (length of wood needed).
# Next line contains N integers denoting height of each tree.

# Ouptut
# Print -1 if it is not possible to cut M meters of wood from all trees else print minimum height H.

# Constraints
# 1 <= N <= 105
# 1 <= M <= 1018
# 1 <= Height of tree <= 109


from typing import List


def woodcutter(n: int, target: int, heights: List[int]) -> int:
    left = 0
    right = max(heights)
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        sum = 0
        for i in heights:
            if i > mid:
                sum += i - mid

        if sum >= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


print("Example 1:", woodcutter(5, 20, [4, 42, 40, 26, 46]))
print("Example 2:", woodcutter(5, 20, [1, 1, 1, 1, 1]))
