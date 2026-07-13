class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        mid = n // 2
        curr = head
        for _ in range(mid):
            curr = curr.next
        return curr