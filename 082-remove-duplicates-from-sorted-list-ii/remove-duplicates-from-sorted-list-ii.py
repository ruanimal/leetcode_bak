# -*- coding:utf-8 -*-


# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_head.next = head
        new_head2 = ListNode(None)
        pointer = new_head
        pointer2 = new_head2
        while pointer.next:
            if pointer.val != pointer.next.val:
                if not pointer.next.next or pointer.next.val != pointer.next.next.val:
                    pointer2.next = pointer.next
                    pointer2 = pointer2.next
            pointer = pointer.next
        pointer2.next = None
        return new_head2.next
