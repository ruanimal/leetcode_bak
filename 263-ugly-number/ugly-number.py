# -*- coding:utf-8 -*-


# Write a program to check whether a given number is an ugly number.
#
#
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
#
#
# Note that 1 is typically treated as an ugly number.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        div_map = [2, 3, 5]
        while num > 1:
            flags = map(lambda x: num%x , div_map)
            try:
                next_act = flags.index(0)
            except ValueError:
                return False
            else:
                return self.isUgly(num/div_map[next_act])
        if num == 1:
            return True
        return False
