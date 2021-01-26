# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 方法：三指针法
        if not head:
            return None
        # 头结点可能被操作，使用哑结点
        dummy_head = ListNode()
        dummy_head.next = head
        # 三指针：prev指向重复部分的前一个结点
        prev = dummy_head
        # start指向重复部分的开始结点
        start = head
        # end指向重复部分的后一个结点
        end = head.next
        while end:
            if start.val == end.val:
                # end向后扫描所有重复结点
                while end and start.val == end.val:
                    end = end.next
                # 删除重复部分
                prev.next = end
                # 将start重新定义为prev的后一个结点
                start = prev.next
                # 如果end不是链表尾，则继续指向下一个结点
                if end:
                    end = end.next
            else:
                # 三指针都前进一步
                prev = prev.next
                start = start.next
                end = end.next

        return dummy_head.next




