from heapq import heapify, heappop


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 可能出现Lists是[[]]的情况，这是True
        # if not lists:
        #     return None
        # 读取所有节点值
        h = []  # 最小堆
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        # 构造一个最小堆
        if not h:
            return None
        heapify(h)  # 转换成最小堆

        # 构造链表
        root = ListNode(heappop(h))
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode

        return root


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next
