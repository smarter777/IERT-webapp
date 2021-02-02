class Solution:
    """
    作者：irruma
    链接：https://leetcode-cn.com/problems/word-break/solution/python3-dong-tai-gui-hua-by-irruma/

    思路：把字符串看错一个小人跳动的过程，字典内的单词看作小人跳跃的规则。

    把小人能够跳跃的过程作为路径，查看所有可能的路径，如果有一条路径能够达到最后，则表示能够拆分。
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            if dp[i] == True:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True

        return dp[-1]

