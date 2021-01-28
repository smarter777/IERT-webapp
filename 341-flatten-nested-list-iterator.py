# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.dfs(nestedList)
        self.i = 0

    def next(self) -> int:
        ret = self.data[self.i]
        self.i += 1
        return ret

    def hasNext(self) -> bool:
        return self.i < len(self.data)

    def dfs(self, nestedList):
        for e in nestedList:
            if e.isInteger():
                self.data.append(e.getInteger())
            else:
                self.dfs(e.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nestedlist):
            for nestedInteger in nestedlist:
                if nestedInteger.isInteger():
                    self.integer.append(nestedInteger.getInteger())
                else:
                    flatten_list(nestedInteger.getList())

        self.integer = []
        flatten_list(nestedList)
        self.position = 0

    def next(self) -> int:
        result = self.integer[self.position]
        self.position += 1
        return result

    def hasNext(self) -> bool:
        if self.position < len(self.integer):
            return True
        else:
            return False
