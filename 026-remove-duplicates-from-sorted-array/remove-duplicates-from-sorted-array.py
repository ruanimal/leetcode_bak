# -*- coding:utf-8 -*-


# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#
#
# For example,
# Given input array nums = [1,1,2],
#
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums <= 1: return len_nums
        to_del = []
        i = 0
        while i < (len_nums -1):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
            if i == len(nums) -1:
                break
        return len(nums)
