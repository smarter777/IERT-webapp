# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next, superior = head, dummy_head
        # 遍历到m的前一个位置 superior (因为需要遍历到前一个位置, 所以最好创建一个虚拟头结点)
        for _ in range(m - 1): # 1. 遍历至m的前一个节点
            superior = superior.next
        # 定义一个节点使其指向m的位置 cur = superior.next
        # 然后就是按照反转链表1的方式直接套就好了. 需要注意一下循环的边界
        # 循环结束之后, 脑海中要浮现出三个指针的位置(浮现个屁, 用纸笔画一下吧骚年)
        # prev 指向n-m的位置,也就是最后一个旋转的节点 cur和next都指向n-m的下一个位置
        cur, prev = superior.next, None
        for _ in range(n - m + 1): # 2. 180°旋转爆炸
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # 最后调整一下superior.next(m处的节点)和prev(n-m位置处)这两个节点的指向即可
        superior.next.next = cur #  3. 修改m和n-m位置处的节点的指向
        superior.next = prev
        return dummy_head.next