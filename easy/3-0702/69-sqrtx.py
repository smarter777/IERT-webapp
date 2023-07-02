class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        a = 0
        ret = x
        mid = -1
        while a < x and x != a + 1:
            #  0 8 0 4
            mid = (a + x) // 2
            # print("a,x,mid",a,x,mid)
            if mid * mid > ret:
                # 4*4 > 8
                x = mid
            else:
                # 2*2 < 8
                a = mid
            # 1 x=3 mid 1
        return a

