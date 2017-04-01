# -*- coding:utf-8 -*-


# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = k
        pq = [None] + nums[:n]
        def sink(k):  # 下沉
            while 2*k <= n:
                j = 2*k
                if j < n and pq[j] > pq[j+1]:
                    j += 1
                if pq[k] <= pq[j]:
                    break
                pq[k], pq[j] = pq[j], pq[k]
                k = j

        for i in xrange(n/2, 0, -1):
            sink(i)
        for i in xrange(n, len(nums)):
            if nums[i] > pq[1]:  # 判断当前值是否比最小值大
                pq[1] = nums[i]
                sink(1)

        while n > 1:
            pq[1], pq[n] = pq[n], pq[1]
            n -= 1
            sink(1)
        return pq[k]
