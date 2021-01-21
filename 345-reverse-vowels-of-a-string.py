class Solution:
    # 对撞指针
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) -1
        s = list(s)
        o_list = ['a','e','i','o','u']
        while l < r:
            if s[r].lower() in o_list and s[l].lower() in o_list:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
            if s[r].lower() not in o_list:
                r -= 1
            if s[l].lower() not in o_list:
                l += 1
        return "".join(s)