class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        for i in range(rowIndex + 1):
            cur_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur_row.append(1)
                else:
                    # print("cur_row", cur_row)
                    cur_row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(cur_row)
        # print("ret", ret)
        return ret[rowIndex]
