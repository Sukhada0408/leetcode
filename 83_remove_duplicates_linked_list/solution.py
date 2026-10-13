# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        prev = head
        current = head.next
        while current!=None:
            if current.val==prev.val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head