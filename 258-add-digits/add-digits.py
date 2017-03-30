# -*- coding:utf-8 -*-

# 将一个数的每一位上的数字加起来，直到只剩下个位数
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 
#
#
#
# For example:
#
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
#
#
#   A naive implementation of the above process is trivial. Could you come up with other methods? 
#   What are all the possible results?
#   How do they occur, periodically or randomly?
#   You may find this Wikipedia article useful.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def func(num):
            result = 0
            for i in str(num):
                result += int(i)
            if num > 10:  # 一轮之后如果大于10，递归
                return func(result)
            else:
                return result
        return func(num)
            
