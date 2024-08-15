# day 3: homework question
# Count digits of a number
def count_digits(nums):
    count = 0
    while nums > 0:
        count += 1
        nums = nums // 10  #  12345 1234 123 12 1 0
        # print(nums)
    return count


num = 123456
# print(count_digits(num))


# Reverse Integer
def reverse_integer(nums):
    res = 0
    while nums > 0:
        # 123 / 10 = 12 will give all digit except last digit
        # 123 % 10 = 3 will give last digit
        res = res * 10 + nums % 10

        nums = nums // 10

    return res


# print(reverse_integer(num))


# Palindrome Number
def is_palindrome(nums):
    # count digit
    while nums > 0:
        #

        nums = nums // 10

    return False


print(is_palindrome(121))
print(is_palindrome(123))


# Add Digits
def add_digits(nums):
    return 0


print(add_digits(123))


# print(123 / 10)
# print(123 % 10)
