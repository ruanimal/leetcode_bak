# -*- coding:utf-8 -*-


# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#
# You must do this in-place without altering the nodes' values.
#
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 

        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        count = length - length/2
        p = p1 = head
        while count > 0:  # 开始移动的指针
            tmp = p
            p = p.next
            count -= 1
        tmp.next = None  # 从中间断开链表
        new_head = ListNode(None)
        new_head.next = p

        tmp = p
        while tmp.next:  # 翻转需要移动的链表
            t = tmp.next
            tmp.next = tmp.next.next
            t.next = new_head.next
            new_head.next = t

        p = new_head.next
        while p:
            tmp1 = p1.next
            tmp = p.next
            p1.next = p
            p.next = tmp1
            p = tmp
            p1 = tmp1

        
