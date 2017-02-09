# -*- coding:utf-8 -*-


# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        point1 = head
        point2 = head

        while 1:
            if point1 and point1.next:
                point1 = point1.next
            else:
                return False
            if point2 and point2.next and point2.next.next:
                point2 = point2.next.next
            else:
                return False
            if point1 == point2:
                return True


