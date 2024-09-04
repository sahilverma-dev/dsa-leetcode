class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def fun(num: int, power=0) -> bool:
            if num <= 0:
                return False
            if num == pow(2, power):
                return True
            elif num < pow(2, power):
                return False
            else:
                return fun(num, power + 1)

        return fun(n)


s = Solution()
print(s.isPowerOfTwo(1))  # True
print(s.isPowerOfTwo(16))  # True
print(s.isPowerOfTwo(3))  # FAlse
