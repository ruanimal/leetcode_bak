# -*- coding:utf-8 -*-

# 罗马数字转阿拉伯数字
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):  # 少循环一次，防止越界
            result += trans_map[s[i]]
            if trans_map[s[i]] < trans_map[s[i+1]]:  # 处理 IV 这种情况
                result -= 2*trans_map[s[i]]
        result += trans_map[s[-1]]  # 把最后一个数字加上
        return result
