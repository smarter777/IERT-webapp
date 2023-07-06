class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        p, q = headA, headB
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            q = q.next
        return None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()
        i, j = headA, headB
        while i:
            hash_set.add(i)
            i = i.next
        while j:
            if j in hash_set:
                return j
            hash_set.add(j)
            j = j.next
        return None
