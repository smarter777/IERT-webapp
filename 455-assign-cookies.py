class Solution:
    """
    排序 + 贪心算法

    双指针法 饼干和胃口都排序 然后移动指针
    当前饼干可以满足当前小孩 则将饼干给小孩 然后i++ j++
    当前饼干不能满足小孩 则找更大的饼干
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count