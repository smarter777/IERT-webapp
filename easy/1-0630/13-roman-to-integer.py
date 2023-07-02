class Solution:
    def romanToInt(self, s: str) -> int:
        map_one = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result = 0
        i = 0
        while i < len(s):
            # 查看当前位和下一位的字符
            str1 = s[i:i + 2]
            # 如果当前位置是特殊情况，那么返回其在字典中对应值，并且下一次从特殊字符之后一位开始索引
            if str1 in map_one:
                result += map_one.get(str1)
                i += 2
            # 如果当前位不是特殊情况，那么只返回当前位的数值
            else:
                result += map_one[s[i]]
                i += 1
        return result
