# -*- coding:utf-8 -*-


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        思路： 将nums2中的逐个插入到nums1合适的位置，调整m的大小，如果某一个nums2中的值大于nums1最后一个值
              则将nums2剩下的值全部添加到nums1后边
        """

        for i in xrange(n):
            for j in xrange(m):
                if nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    m += 1
                    break
                if m == len(nums1):
                    return
            else:
                for k, num in enumerate(nums2[i:]):
                    nums1[m+k] = num
                return
