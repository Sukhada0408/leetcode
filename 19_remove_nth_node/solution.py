# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        remove = head
        prev = head
        ind = count-n
        if count==1:
            head = None
        elif count>1 and ind==0:
            head = head.next
        for i in range(ind-1):
            prev = prev.next
            remove  = remove.next
        if remove!=None:
            if remove.next!=None:
                remove = remove.next
                prev.next = remove.next
            else:
                prev.next = None
        else:
            prev.next==None
        return head