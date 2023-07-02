class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_arr = list(s)
        i = 0
        for one in s_arr[::-1]:
            if one == ' ':
                break
            i += 1
        return i


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        return len(s.split(" ")[-1])
