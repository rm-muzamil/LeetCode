class Solution(object):
    def twoSum(self, nums, target):
      result = {}
      for i,num in enumerate(nums):
        complement = target - num
        if complement in result:
            return [result[complement], i]
        result[num] = i

        