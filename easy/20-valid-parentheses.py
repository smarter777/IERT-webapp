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


class Solution:
    def is_match(self, one, two):
        if one == '(' and two == ')':
            return True
        elif one == '[' and two == ']':
            return True
        elif one == '{' and two == '}':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            # 如果栈顶 与当前的匹配
            if stack and self.is_match(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        if len(stack) == 0:
            return True
        else:
            return False
