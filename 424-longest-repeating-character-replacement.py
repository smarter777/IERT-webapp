class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        m = 0
        for a in d.values():
            i = 0
            for j in range(m + 1, len(a)):
                if j - i <= m:
                    continue
                t = a[j] - j - k
                while a[i] - i < t:
                    i += 1
                m = max(m, j - i)
        return min(len(s), m + k + 1)


class Solution:
    """
    https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-n6aza/
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26  # 代替哈希表记录当前每个大写字母的重复数
        n = len(s)
        maxcount = left = right = 0  # 左右指针与当前区间内重复字符中的最大重复数
        res = 0  # 用来记录当前符合条件的最大窗口长度
        while right < n:
            count[ord(s[right]) - ord("A")] += 1  # 碰到新字符记录下来
            maxcount = max(count)  # 判断当前加入新字符的区间内重复字符中的最大重复数
            if right - left + 1 - maxcount > k:  # 判断剩余字符的数量是否大于k，若大于k则说明可替换的字符不够，需要移动左指针收缩区间
                count[ord(s[left]) - ord("A")] -= 1  # 去掉移动出去的左边界
                left += 1
            right += 1
            res = max(res, right - left)  # 不断记录最大的区间长度
        return res
