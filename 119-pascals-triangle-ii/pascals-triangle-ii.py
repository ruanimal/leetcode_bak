# -*- coding:utf-8 -*-

# 给定一个数字k，就帕斯卡三角的第k行
# Given an index k, return the kth row of the Pascal's triangle.
#
#
# For example, given k = 3,
# Return [1,3,3,1].
#
#
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution(object):
    map_dict = {0:[1], 1:[1,1]}  # 用字典记录每一行的值，进行递归优化
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex in Solution.map_dict:  # 如果该行在字典中就直接返回，降低复杂度
            return Solution.map_dict[rowIndex]
        tmp = [1]
        for i in xrange(1, rowIndex):
            tmp.append(self.getRow(rowIndex-1)[i-1] + self.getRow(rowIndex-1)[i])  # 递归计算，如果不采用map_dict,复杂度应该是n*2^n
        tmp.append(1)
        Solution.map_dict[rowIndex] = tmp
        return tmp

        

