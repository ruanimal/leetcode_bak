# -*- coding:utf-8 -*-


# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
#
#
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
#
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        end = len(nums) -1
        x = 0
        while x < end:
            if nums[x] == 0:
                del nums[x]
                nums.append(0)
                x -= 1
                end -= 1
            x += 1
