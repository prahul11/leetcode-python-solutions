# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next  
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
    

class Solution:
    def mergeTwoLists(self, l1, l2):
        d = ListNode()
        curr = d

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr =  l1
                l1 = l1.next
                
            else:
                curr.next = l2
                curr =  l2
                l2 = l2.next
                
        curr.next =  l1 if l1 else l2
        return d.next