# -*- coding:utf-8 -*-


# Implement strStr().
#
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
