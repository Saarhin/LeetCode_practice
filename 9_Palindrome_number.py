class Solution:
    def isPalindrome(self, x: int) -> bool:

        str_1 = str(x)
        str_2 = str_1[::-1]

        if str_1 == str_2:
            return True
        return False