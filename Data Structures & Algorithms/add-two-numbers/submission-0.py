class Solution:
    def reverse(self, head):
        pre = None
        curr = head
        while curr != None:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2

        newlist = None
        carry = 0
        while num1 != None or num2 != None or carry > 0:
            val = carry 
            if num1 != None:
                val += num1.val
                num1 = num1.next
            if num2 != None:
                val += num2.val
                num2 = num2.next
            nval = val % 10
            carry = val // 10

            newNode = ListNode(nval)
            newNode.next = newlist
            newlist = newNode
        return self.reverse(newlist)