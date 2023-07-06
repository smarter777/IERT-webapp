class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        multiple = 1
        columnTitle = list(columnTitle)
        for index, one in enumerate(columnTitle[::-1]):
            ret += (ord(one) - 64) * multiple
            multiple *= 26
            print("ret", ret)
        return ret


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        columnTitle = list(columnTitle)
        for index, one in enumerate(columnTitle[::-1]):
            ret += (ord(one) - 64) * 26 ** index
            print("ret", ret)
        return ret
