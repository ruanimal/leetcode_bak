# -*- coding:utf-8 -*-


# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists: 
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#
# Credits:Special thanks to @stellari for adding this problem and creating all test cases.


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not (headA and headB): return
        if headA == headB: return headA
        if headA.next == headB.next: return headA.next

        count_a = 0
        count_b = 0
        pointer1 = headA
        pointer2 = headB

        while pointer1.next:
            count_a += 1
            pointer1 = pointer1.next
        while pointer2.next:
            count_b += 1
            pointer2 = pointer2.next
        if pointer1 != pointer2:
            return 

        pointer1 = headA
        pointer2 = headB
        while count_a > count_b:
            pointer1 = pointer1.next
            count_a -= 1
        while count_a < count_b:
            pointer2 = pointer2.next
            count_b -= 1
        while pointer1 and pointer2:
            if pointer1 == pointer2:
                return pointer1
            else:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
