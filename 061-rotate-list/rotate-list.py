# -*- coding:utf-8 -*-

# 给定一个链表，左移k位
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1 2 3
        if not head: 
            return
        # 求链表长度
        count = 1
        p = head
        while p.next:
            p = p.next
            count += 1
        # 将链表连成环
        p.next = head
        # 求出真正需要移动的位数
        k = count - (k % count)
        # 求出新起点
        while k > -1:
            p = p.next
            k -= 1
        new_head = p
        # 求出新终点
        while count > 1:
            p = p.next
            count -= 1
        p.next = None
        return new_head
