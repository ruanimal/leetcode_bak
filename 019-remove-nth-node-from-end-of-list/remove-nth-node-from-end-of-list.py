# -*- coding:utf-8 -*-


# Given a linked list, remove the nth node from the end of list and return its head.
#
#
# For example,
#
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return

        new_head = ListNode(None)
        new_head.next = head
        pointer1 = pointer2 = new_head
        while n > 0:
            pointer1 = pointer1.next
            n -= 1
        while pointer1.next:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        pointer2.next = pointer2.next.next
        return new_head.next

