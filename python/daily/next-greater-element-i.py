# https://leetcode.com/problems/next-greater-element-i/description/


from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []


    

    for i in nums1:
        if i in nums2:
            print(i)
        else:
            ans.append(-1)
    return ans


print(
    "Example 1:", nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
)  # [-1,3,-1]
print("Example 2:", nextGreaterElement([2, 4], nums2=[1, 2, 3, 4]))  # [3,-1]
# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
