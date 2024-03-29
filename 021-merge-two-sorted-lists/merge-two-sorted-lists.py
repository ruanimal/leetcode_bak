# -*- coding:utf-8 -*-


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        while l1 and l2:
            if l1.val > l2.val:
                result.append(l2.val)
                l2 = l2.next
            else:
                result.append(l1.val)
                l1 = l1.next

        aa = l1 or l2 or 0
        while aa:
            result.append(aa.val)
            aa = aa.next
        return result


