class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f1 = lambda a,b:a+b
        f2 = lambda a,b:a-b
        f3 = lambda a,b:a*b
        f4 = lambda a,b:int(a/b)
        maps = {'+':f1,'-':f2,'*':f3,'/':f4}
        stack = []
        for t in tokens:
            # print(stack)
            if t in maps:
                a = stack.pop()
                b = stack.pop()
                stack.append(maps[t](b,a))
            else:
                t = int(t)
                stack.append(t)
        return stack.pop()

