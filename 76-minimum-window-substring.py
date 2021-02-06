class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        # [left, right) 是窗口
        # 1- 先不断地增加 right 指针扩大窗口 [left, right);
        #    直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
        # 2- 我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right)
        #    直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了） 每次增加 left，我们都要更新一轮结果
        # 3- 重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头
        # 第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解
        # 左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        window = collections.defaultdict(int)
        # valid 变量表示窗口中满足 need 条件的字符个数，如果 valid 和 need.size 的大小相同
        # 窗口已满足条件，已经完全覆盖了串 T
        valid = 0

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        sub_len = float('inf')
        while right < len(s):
            # 开始滑动 c 是将移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < sub_len:
                    start = left
                    sub_len = right - left

                # d 是移出窗口的字符
                d = s[left]

                # 窗口缩小
                left += 1

                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 返回最小覆盖子串
        print(start, sub_len)
        return "" if sub_len == float('inf') else s[start:start + sub_len]


class Solution:
    """
    链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
    """

    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果
