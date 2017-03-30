# -*- coding:utf-8 -*-

# 判断一个数是否是2的次方
# Given an integer, write a function to determine if it is a power of two.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfTwo(self, n):
        """计算1第个数，次方数有且只有第一位为1；还有一种解法是把2的0到32次方都算出来，除此之外的都不是
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)
        if bin_n[2] == '1' and bin_n.count('1') == 1:
            return True
        return False
