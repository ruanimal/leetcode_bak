# -*- coding:utf-8 -*-


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in ']})':
                if not stack:
                    return False
                elif stack.pop() != d[i]:
                    return False
        return False if stack else True
