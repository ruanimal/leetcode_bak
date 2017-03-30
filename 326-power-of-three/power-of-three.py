# -*- coding:utf-8 -*-

# 判断一个数是否是3的幂
# Given an integer, write a function to determine if it is a power of three.
#
#
#     Follow up:
#     Could you do it without using any loop / recursion?
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfThree(self, n):
        """1162261467 是最大的3的幂（int）
        :type n: int
        :rtype: bool
        """
        return (n > 0 and 1162261467 % n == 0);
