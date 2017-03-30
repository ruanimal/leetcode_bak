# -*- coding:utf-8 -*-

# 给定一个链表，判断环开始的位置
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
#
#
# Note: Do not modify the linked list.
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
    def detectCycle(self, head):
        """快慢指针，先找到环上的相遇点，'相遇点到环的起始点的距离'和'链表起点到环的起始点的距离'相等
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return

        p1 = p2 = head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                break
        else:
            return
        p1 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
