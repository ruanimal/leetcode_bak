# -*- coding:utf-8 -*-


# Sort a linked list in O(n log n) time using constant space complexity.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge_sort(head):
            length = 0
            pp = p1 = p2 = head
            while p1 and p2:
                pp = p1
                p1 = p1.next
                if p2.next:
                    p2 = p2.next.next
                    length += 2
                else:
                    p2 = p2.next
                    length += 1
                    break
            if pp:
                pp.next = None
            if length <= 1:
                return head
            left = merge_sort(head)
            right = merge_sort(p1)
            return merge(left, right)

        def merge(left, right):
            import pdb
            left_p = left
            right_p = right
            head = ListNode(None)
            head_p = head
            # pdb.set_trace()
            while left_p and right_p:
                if left_p.val < right_p.val:
                    head_p.next = left_p
                    left_p = left_p.next
                else:
                    head_p.next = right_p
                    right_p = right_p.next
                head_p = head_p.next
        
            while left_p:
                head_p.next = left_p
                left_p = left_p.next
                head_p = head_p.next
        
            while right_p:
                head_p.next = right_p
                head_p = head_p.next
                right_p = right_p.next
            return head.next
            
        return merge_sort(head)
