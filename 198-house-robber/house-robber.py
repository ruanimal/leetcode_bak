# -*- coding:utf-8 -*-


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.


class Solution(object):
    def rob(self, nums, money=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return money + nums[0]
        elif len(nums) == 2:
            return money + max(nums)
        else:
            if nums[0] >= nums[1]:
                money += nums[0]
                return self.rob(nums[2:], money)
            else:
                nums[2] = nums[0] + nums[2]
                return self.rob(nums[1:], money)
