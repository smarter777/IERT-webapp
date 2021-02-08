class Solution:
    """
    作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode-solution/
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快指针走到末尾，慢指针刚好到中间。其中慢指针将前半部分反转。然后比较
        # 这道题目非常经典，有几个需要注意的地方
        # 1、找到链表的中点，可以使用快慢指针；（最开始想的办法是遍历长度除以2）
        # 2、在找链表中点的时候，就顺带把前半部分的链表反转了
        # 3、进行对比，注意，此时需要考虑链表长度是基偶，处理会有差异，见下面的代码
        # 4、最开始 快慢指针都指向head，在while循环里面 一定要把fast的移动放在前面，不同slow移动的时候，会有空指针出现
        fast, slow = head, head
        pre = None
        while fast and fast.next:
            # fast移动要放在前面
            fast = fast.next.next
            temp = slow.next
            # 如果fast移动放在后面时，下面的这行代码执行时，就已经把fast.next置为pre(None)了
            # 所以在第一个循环就会报错（为啥？因为fast和slow此时都指向head）
            slow.next = pre
            pre = slow
            slow = temp

        # 奇偶通过这个来判断，如果链表长度为3 则快指针走一步，刚好fast不为空 此时slow要往后一步
        # 如果长度为2 那么fast肯定是为None的
        if fast:
            slow = slow.next
        while pre and slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next

        return True
