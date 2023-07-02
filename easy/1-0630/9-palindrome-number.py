class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_arr = list(str(x))
        for one, end_one in zip(x_arr, x_arr[::-1]):
            if one != end_one:
                return False
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        beg = 0
        s = str(x)
        beg, end = 0, len(s) - 1
        while beg < end:
            if s[beg] == s[end]:
                beg += 1
                end -= 1
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 双向指针
        x_str = str(x)
        s_p = 0
        e_p = len(x_str)-1
        while s_p < e_p:
            if x_str[s_p] == x_str[e_p]:
                s_p += 1
                e_p -= 1
            else:
                return False
        return True