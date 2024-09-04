def get_flipped_binary(num):
    binary = []

    def fun(n):
        if n == 0:
            return
        fun(n // 2)
        binary.append(n % 2)

    fun(num)
    return binary

    # return binary


class Solution:
    def findComplement(self, num: int) -> int:
        # lol = (
        #     bin(num)
        #     .replace("0b", "")
        #     .replace("1", "t")
        #     .replace("0", "1")
        #     .replace("t", "0")
        # )

        # return int(lol, 2)
        binary = get_flipped_binary(num)
        print(binary)
        return 0


s = Solution()


print(s.findComplement(5))  # 2
# print(s.findComplement(1))  # 0
