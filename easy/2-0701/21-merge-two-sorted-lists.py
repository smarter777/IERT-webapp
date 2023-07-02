# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        cur = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy_head.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node
        # l1或者12可能还有剩余元素
        # if l1 is None:
        #     cur.next = l2
        # else:
        #     cur.next = l1
        cur.next = l1 or l2
        return root.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 两个指针，谁小谁往前移动
        point1 = list1
        point2 = list2
        root = ListNode(None)
        merge_list = root
        return_flag = True
        while point1 and point2:
            if point1.val <= point2.val:
                merge_list.next = ListNode(val=point1.val)
                point1 = point1.next
                merge_list = merge_list.next
            else:
                merge_list.next = ListNode(val=point2.val)
                point2 = point2.next
                merge_list = merge_list.next
        # print("pointxxx",point1,point2)
        if point1:
            merge_list.next = point1
            merge_list = merge_list.next
        if point2:
            merge_list.next = point2
            merge_list = merge_list.next
        # print("root", root)
        return root.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2