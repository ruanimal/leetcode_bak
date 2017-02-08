# -*- coding:utf-8 -*-


# Given numRows, generate the first numRows of Pascal's triangle.
#
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1: return []
        if numRows == 1: return [[1],]
        lst = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        return lst
