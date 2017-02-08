# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def reverse_link(node):
            head = ListNode(None)
            head.next = node
            while node.next is not None:
                tmp = node.next
                node.next = node.next.next
                head.next, tmp.next = tmp, head.next
            return head.next

        l1 = reverse_link(l1)
        l2 = reverse_link(l2)
        result = ListNode(None)
        tmp = 0
        while l1 or l2 or tmp != 0:
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmp, b = divmod(tmp, 10)
            tmp2 = result.next
            result.next = ListNode(b)
            result.next.next = tmp2
 
        return result.next 

