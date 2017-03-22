# -*- coding:utf-8 -*-


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
    map_dict = {0:[1], 1:[1,1]}
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex in Solution.map_dict:
            return Solution.map_dict[rowIndex]
        tmp = [1]
        for i in xrange(1, rowIndex):
            tmp.append(self.getRow(rowIndex-1)[i-1] + self.getRow(rowIndex-1)[i])
        tmp.append(1)
        Solution.map_dict[rowIndex] = tmp
        return tmp

        

