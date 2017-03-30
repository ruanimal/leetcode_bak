# -*- coding:utf-8 -*-

# 以O(log (m+n)) 复杂度求两个已排序列表的中位数
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
        """先将两个list merge到一起，然后算出中位数的位置
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
        if len(result)%2==1:  # 合并后list长度为奇数
            return result[len(result)//2]
        else:
            return  (result[len(result)//2-1]+result[len(result)//2])/2.0
