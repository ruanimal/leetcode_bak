# -*- coding:utf-8 -*-

# 判断括号字符串的合法性
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """通过栈来实现，遇到左括号入栈，遇到右括号则出栈，判断是否匹配。
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
        return False if stack else True  # 结束时栈不为空
