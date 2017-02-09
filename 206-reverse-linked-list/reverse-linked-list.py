# -*- coding:utf-8 -*-


# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return
        new_head = ListNode(None)
        new_head.next = head
        pointer = head
        while pointer.next:
            tmp = pointer.next
            pointer.next = pointer.next.next
            tmp.next = new_head.next
            new_head.next = tmp
        return new_head.next 

