# https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.


# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# Example 2:

# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# Since not every customer received the correct change, the answer is false.
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash_map = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                hash_map[5] += 1
            elif bill == 10:

                if hash_map[5] > 0:
                    hash_map[5] -= 1
                    hash_map[10] += 1
                else:
                    return False
            elif bill == 20:

                if hash_map[10] > 0 and hash_map[5] > 0:
                    hash_map[10] -= 1
                    hash_map[5] -= 1

                elif hash_map[5] >= 3:
                    hash_map[5] -= 3
                else:
                    return False

        return True


s = Solution()

print("Example 1:", s.lemonadeChange([5, 5, 5, 10, 20]))  # True
print("Example 1:", s.lemonadeChange([5, 5, 10, 10, 20]))  # False
