class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, num = divmod(columnNumber, 26)
            ret = chr(65 + num) + ret
        return ret


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, rest = divmod(columnNumber, 26)
            ret = chr(65 + rest) + ret
        return ret
