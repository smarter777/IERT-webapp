class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p not in ["", ".", ".."]:
                stack.append(p)
            elif p == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split('/'):
            if s == "..":
                if stack:
                    stack.pop()
            elif s and s != '.':
                stack.append(s)
        return '/' + '/'.join(stack)
