# -*- coding:utf-8 -*-


# Write a function that takes a string as input and reverse only the vowels of a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        string_list = list(s)
        vowels_list = [i for i, e in enumerate(s) if e in 'aeiouAEIOU']
        i = 0
        while i < len(vowels_list)/2:
            string_list[vowels_list[i]], string_list[vowels_list[-i-1]] = string_list[vowels_list[-i-1]], string_list[vowels_list[i]]
            i += 1
        return ''.join(string_list)
