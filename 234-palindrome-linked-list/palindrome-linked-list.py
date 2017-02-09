# -*- coding:utf-8 -*-


# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        if count < 2:
            return True

        half, add = divmod(count, 2)
        half -= 1
        new_head = ListNode(None)
        new_head.next = head
        while half > 0:
            tmp = head.next
            head.next = head.next.next
            tmp.next = new_head.next
            new_head.next = tmp
            half -= 1
        p1 = new_head
        p2 = head.next if add else head
        p1 = p1.next
        p2 = p2.next
        half = count/2
        while half > 0:
            half -= 1
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next 
            else:
                return False
        return True
