# -*- coding:utf-8 -*-

# 求list中出现次数最多的元素，最多的元素至少出现floor(n/2)次
# Given an array of size n, find the majority element. The majority element is the element that appears more than &lfloor; n/2 &rfloor; times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def majorityElement(self, nums):
        """先排序，然后统计连续元素的个数
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 or (n == 2 and nums[0] == nums[1]): 
            return nums[0]

        nums.sort()
        count = 1
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                count = 1
            if count > n/2.0:
                return nums[i]
            
            
        
        
