# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode() 
        _resultRoot = result
        carry = 0
        while True:
            result.val = l1.val + l2.val + carry
            carry = result.val//10
            result.val = result.val%10
            l1 = l1.next
            l2 = l2.next
            result.next = ListNode()
            if l1 == None or  l2 == None:
                break
            result = result.next

        if l1 != None:
           result, carry = self.copyLinkedListWithCarry(l1, result, carry)
        elif l2 != None:
           result, carry = self.copyLinkedListWithCarry(l2, result, carry)
    
        if carry == 1:
            result = result.next
            result.val = 1
        
        result.next = None

        return _resultRoot

    def copyLinkedListWithCarry(self, l, result, carry):
        result = result.next
        while True:
            result.val = l.val + carry
            carry = result.val//10
            result.val = result.val%10
            l = l.next
            result.next = ListNode()
            if l == None:
                break
            result = result.next
        return result, carry
       

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

s = Solution()
#[9,9,9,9,9,9,9]
#[9,9,9,9]
#n1 = ListNode(2, ListNode(4, ListNode(3, None)))
#n2 = ListNode(5, ListNode(6, ListNode(4, None)))
#n1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
#n2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
n1 = ListNode(9, ListNode(9, ListNode(1,  None)))
n2 = ListNode(1, None)
#n1 = ListNode(0, None)
#n2 = ListNode(0, None)
p = s.addTwoNumbers(n1, n2)
while p != None: 
    print(p.val); 
    p=p.next