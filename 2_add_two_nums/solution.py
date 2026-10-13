# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = 0
        num2 = 0
        curr = l1
        i=0
        while curr!=None:
            num1 += curr.val*(10**(i))
            i+=1
            curr = curr.next
        i=0
        curr = l2
        while curr!=None:
            num2 += curr.val*(10**(i))
            i+=1
            curr = curr.next
        sum = num1+num2
        digit = sum%10
        sum = sum//10
        prev = ListNode(digit)
        head = prev
        while sum!=0:
            digit = sum%10
            sum = sum//10
            curr = ListNode(digit)
            prev.next = curr
            prev = curr
        return head
