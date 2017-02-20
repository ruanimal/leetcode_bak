# -*- coding:utf-8 -*-


# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
#
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
#
# For example,
# Given this linked list: 1->2->3->4->5
#
#
#
# For k = 2, you should return: 2->1->4->3->5
#
#
#
# For k = 3, you should return: 3->2->1->4->5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        思路：每次反转k个链表，如果不满k个则说明到达末尾，对这一次重新反转使之保持原有顺序
        """
        if not head or k <= 1:
            return head

        new_head = ListNode(None)
        new_head.next = head
        pointer1 = new_head.next
        pointer2 = new_head
        while pointer1:
            try:
                for _ in range(k-1):
                    tmp = pointer1.next
                    pointer1.next = pointer1.next.next
                    tmp.next = pointer2.next
                    pointer2.next = tmp
            except AttributeError:
                pointer1 = pointer2.next
                while pointer1.next:
                    tmp = pointer1.next
                    pointer1.next = pointer1.next.next
                    tmp.next = pointer2.next
                    pointer2.next = tmp
                break
            pointer2 = pointer1
            pointer1 = pointer1.next
        return new_head.next
