# -*- coding:utf-8 -*-

# 判断两个字符串是否由同样的字母组成
# Given two strings s and t, write a function to determine if t is an anagram of s. 
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = [x for x in s]
        tl = [x for x in t]
        sl.sort()
        tl.sort()
        if sl==tl:
            return True
        else:
            return False
            
        
