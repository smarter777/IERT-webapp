from typing import List


class Solution:
    def same(self, freq_1, freq_2):
        for i in range(26):
            if freq_1[i] != freq_2[i]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = [0 for i in range(26)]
        freq_s = [0 for i in range(26)]
        res = []
        for c in p:
            freq_p[ord(c) - ord('a')] += 1
        l = 0
        r = -1  # Sliding window: s[l, r]
        while r + 1 < len(s):
            r += 1
            freq_s[ord(s[r]) - ord('a')] += 1;
            if r - l + 1 > len(p):
                freq_s[ord(s[l]) - ord('a')] -= 1
                l += 1

            if r - l + 1 == len(p) and self.same(freq_s, freq_p):
                res.append(l)
        return res
