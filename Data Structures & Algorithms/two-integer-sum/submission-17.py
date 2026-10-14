class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in nums and i != nums.index(second_num):
                return sorted([i, nums.index(second_num)])