# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        number1 = l1.val if l1 else 0
        number2 = l2.val if l2 else 0
        sum = number1 + number2 + carry

        node = ListNode(sum % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            sum // 10
        )
        return node
    
"""
This is just adding by hand 🤷‍♂️

    3 4 2
   +
    4 6 5
   -------
    8 0 7
"""












