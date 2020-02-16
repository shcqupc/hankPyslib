# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


n1 = ListNode("1->2->4")
n2 = ListNode("1->3->4")
print(n1.val, n2.val)
s = Solution()
rslt = s.mergeTwoLists(n1, n2)
print(rslt.val)
