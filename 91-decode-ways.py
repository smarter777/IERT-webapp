class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):  # 开头有 ‘0’ 直接返回
            return 0

        n = len(s)
        dp = [1] * (n + 1)  # 重点是 dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            if s[i - 1] == '0' and s[i - 2] not in '12':  # 出现前导 ‘0’ 的情况，不能解码，直接返回
                return 0
            if s[i - 2:i] in ['10', '20']:  # 只有组合在一起才能解码
                dp[i] = dp[i - 2]
            elif '10' < s[i - 2:i] <= '26':  # 两种解码方式
                dp[i] = dp[i - 1] + dp[i - 2]
            else:  # '01'到 ‘09’ 或 > '26'，只有单独才能解码
                dp[i] = dp[i - 1]
        return dp[n]


class Solution:
    def numDecodings(self, s: str) -> int:
        cnt = [1, 1] + [0] * len(s)
        s = "99" + s  # 添加虚拟头部，以便不用对头部做特殊处理
        for i in range(2, len(s)):
            if (10 <= int(s[i - 1:i + 1]) <= 26):  # s[i]可与s[i-1]组合
                cnt[i] += cnt[i - 2]
            if (s[i] != '0'):  # s[i]可单独解码
                cnt[i] += cnt[i - 1]
        return cnt[-1]
