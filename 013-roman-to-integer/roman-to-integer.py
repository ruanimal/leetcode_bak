# -*- coding:utf-8 -*-


# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            result += map[s[i]]
            if map[s[i]] < map[s[i+1]]:
                result -= 2*map[s[i]]
        result += map[s[-1]]
        return result
