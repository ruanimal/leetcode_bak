# -*- coding:utf-8 -*-

# 这道题的要求是给定一个数组表示非负整数，其高位在数组的前面，对这个整数加1。
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        addtion = 1
        for i in range(len(digits)-1, -1, -1):
            if addtion:  #　此处其实可以用divmod来计算进位
                if digits[i] >= 9:
                    digits[i] = 0
                    addtion = 1
                else:
                    digits[i] += 1
                    addtion = 0
        if addtion:
            digits.insert(0, 1)
        return digits
