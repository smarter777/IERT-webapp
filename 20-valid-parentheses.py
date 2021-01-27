class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            flag = True
            for right, left in char_map.items():
                if s[i] == right and stack[-1:] == [left]:
                    stack.pop()
                    flag = False
            if flag:
                stack.append(s[i])
        return bool(len(stack) == 0)

