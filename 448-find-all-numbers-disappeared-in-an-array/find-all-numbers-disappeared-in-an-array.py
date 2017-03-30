# -*- coding:utf-8 -*-

# 给定一个list，有的元素出现两次，元素的取值范围是 1 ≤ a[i] ≤ n，有的没有出现，求没出现的元素
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        tmp = {i:0 for i in xrange(1, len(nums)+1)}
        for num in nums:
            tmp[num] = 1
        return [key for key,val in tmp.iteritems() if val == 0] 
