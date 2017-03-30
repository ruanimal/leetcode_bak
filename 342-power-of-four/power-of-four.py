# -*- coding:utf-8 -*-

# 判断4的幂
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfFour(self, num):
        """查表法
        :type num: int
        :rtype: bool
        """
        powers = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        return num in powers
