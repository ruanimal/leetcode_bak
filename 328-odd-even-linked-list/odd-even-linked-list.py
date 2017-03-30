# -*- coding:utf-8 -*-

# 将链表的位置为偶数的节点放到奇数节点后面
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
#
#
# Note:
# The relative order inside both the even and odd groups should remain as it was in the input. 
# The first node is considered odd, the second node even and so on ...
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """将偶数节点全部取出到一个新链表上，然后连到链表后面
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        new_head = ListNode(None)
        p1 = head
        p2 = new_head
        while p1 and p1.next:
            p2.next = p1.next
            p1.next = p1.next.next
            if p1.next is not None:
                p1 = p1.next
            p2 = p2.next
        p2.next = None
        p1.next = new_head.next
        return head
        
