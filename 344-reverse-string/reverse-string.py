# -*- coding:utf-8 -*-


# Write a function that takes a string as input and returns the string reversed.
#
#
# Example:
# Given s = "hello", return "olleh".


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <2: return s
        return ''.join(list(s)[::-1])
