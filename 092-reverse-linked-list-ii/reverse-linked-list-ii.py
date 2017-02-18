# -*- coding:utf-8 -*-


# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
#
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#
# return 1->4->3->2->5->NULL.
#
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or n==m:
            return head
        new_head = ListNode(None)
        new_head.next = head
        pointer = new_head
        for i in xrange(m-1):
            pointer = pointer.next
        pointer2 = pointer.next
        for i in xrange(n-m):
            tmp = pointer2.next
            pointer2.next = pointer2.next.next
            tmp.next = pointer.next
            pointer.next = tmp
        return new_head.next


        
