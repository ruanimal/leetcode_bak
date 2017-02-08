# -*- coding:utf-8 -*-


# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        l = r = 0
        while l<len(nums1) and r<len(nums2):
            if nums1[l] < nums2[r]:
                result.append(nums1[l])
                l += 1
            else:
                result.append(nums2[r])
                r += 1
        result += nums1[l:]
        result += nums2[r:]
        if len(result)%2==1:
            return result[len(result)//2]
        else:
            return  (result[len(result)//2-1]+result[len(result)//2])/2.0
