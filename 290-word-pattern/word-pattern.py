# -*- coding:utf-8 -*-


# Given a pattern and a string str, find if str follows the same pattern.
#  Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
#
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
#
#
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
#
#
# Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(set(pattern)) != len(set(words)): return False
        p_len = len(pattern)
        w_len = len(words)
        if p_len < 1 or w_len <1 or p_len != w_len : return False
        for i in range(p_len-1):
            for j in range(i+1, p_len):
                if (pattern[j] == pattern[i] and words[j] != words[i]):
                    return False
        return True
            
            
