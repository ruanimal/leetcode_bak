# -*- coding:utf-8 -*-


# Given an integer, write a function to determine if it is a power of two.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)
        if bin_n[2] == '1' and bin_n.count('1') == 1:
            return True
        return False
