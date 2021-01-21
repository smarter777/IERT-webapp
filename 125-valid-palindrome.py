class Solution:
    # 对撞指针
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l +=1
                r -=1
            else:
                return False
        return True