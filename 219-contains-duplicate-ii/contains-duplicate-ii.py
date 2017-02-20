# -*- coding:utf-8 -*-


# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}
        for i, ele in enumerate(nums):
            index_map.setdefault(ele, []).append(i)
        for key, val in index_map.iteritems():
            if len(val) >= 2:
                val.sort()
                for i in xrange(len(val)-1):
                    if val[i+1] - val[i] <= k:
                        return True
        return False
