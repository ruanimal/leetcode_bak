# -*- coding:utf-8 -*-

# 给定一个数字，求对应行数的帕斯卡三角
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
        lst = [[1]*i for i in range(1, numRows+1)]  # 构造出所有值为1的帕斯卡三角
        for i in range(2, numRows): # 从第3行开始计算内部对应的值
            for j in range(1, i):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]  # 这一行第j个数字的值等于上一行的第j-1加j
        return lst
