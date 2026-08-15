# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst= []
        Newhead = dummy = ListNode()
        curr = dummy
        while head!= None:
            lst.append(head.val)
            head = head.next
        lst.pop(-n)
        for i in lst:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
