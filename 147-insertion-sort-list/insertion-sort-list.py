# -*- coding:utf-8 -*-

# 使用插入排序，排序链表
# Sort a linked list using insertion sort.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        new_head = ListNode(None)
        new_head.next = head   # 已排序头部
        tail = head  # 已排序尾巴

        while tail.next:
            tmp = tail.next
            tail.next = None
            p = new_head
            while p != tail:
                if p.next.val < tmp.val:
                    p = p.next
                else:
                    tail.next = tmp.next  #新元素插在队伍中间
                    tmp.next = p.next
                    p.next = tmp
                    break
            else:
                tail.next = tmp  # 新元素插在队尾
                tail = tail.next

        return new_head.next
        
