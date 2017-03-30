# -*- coding:utf-8 -*-

# 给定一个链表，将所有小于k的节点放到大于等于k的节点前面
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """将链表分成大于k和小于k的两个链表，然后将两链表连起来
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        small = ListNode(None)
        small.next = head
        big = ListNode(None)
        pointer = small
        pointer1 = big
        while pointer.next:
            if pointer.next.val >= x:
                pointer1.next = pointer.next
                pointer.next = pointer.next.next
                pointer1 = pointer1.next
            else:
                pointer = pointer.next
        pointer.next = big.next
        pointer1.next = None   # 清除多余的后继，防止链表循环

        return small.next
        
