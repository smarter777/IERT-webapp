class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        common_prefix = ''
        for i in range(len(strs[0])):
            one_c = strs[0][i]
            for one in strs[1:]:
                if one[i] != one_c:
                    return common_prefix
            common_prefix += one_c
        return common_prefix