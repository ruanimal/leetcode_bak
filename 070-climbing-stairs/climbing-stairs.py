# -*- coding:utf-8 -*-


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
# Note: Given n will be a positive integer.


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        a = b = 1
        for i in range(1, n):
            a, b = b, a + b
        return b
        
