class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        映射是双向的，上下都得判断一遍
        """
        rela_map = {}
        rever_map = {}
        for s_i,t_i in zip(s,t):
            if s_i not in rela_map:
                rela_map[s_i] = t_i
            elif s_i in rela_map:
                if rela_map[s_i] != t_i:
                    return False
            if t_i not in rever_map:
                rever_map[t_i] = s_i
            elif t_i in rever_map:
                if rever_map[t_i] != s_i:
                    return False
        return True
