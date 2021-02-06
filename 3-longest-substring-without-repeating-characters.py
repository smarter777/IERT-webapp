class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        window = collections.defaultdict(int)
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            window[c] += 1

            # 判断左侧窗口是否要收缩, 排列长度和s1长度一样
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            # 这里更新答案
            res = max(res, right - left)
        # 未找到符合条件的子串
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
