# -*- coding:utf-8 -*-

# 将链表的相邻的两个节点对调
# Given a linked list, swap every two adjacent nodes and return its head.
#
#
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """此处采用直接对调值的做法，指针步长为2
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = head
        while pointer and pointer.next is not None:
            pointer.val, pointer.next.val = pointer.next.val, pointer.val
            pointer = pointer.next.next
        return head

