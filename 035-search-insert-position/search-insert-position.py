# -*- coding:utf-8 -*-

# 给定一个target和一个有序list，判断target是否在list中，是者返回index，否则返回应该在的位置
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
#
# Here are few examples.
# [1,3,5,6], 5 &#8594; 2
# [1,3,5,6], 2 &#8594; 1
# [1,3,5,6], 7 &#8594; 4
# [1,3,5,6], 0 &#8594; 0


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        try:
            return nums.index(target)
        except ValueError:
            for i, ele in enumerate(nums):
                if target < ele:  # 找到收个大于target的位置
                    return i
            else:  # 如果找不到就在末尾
                return i + 1
