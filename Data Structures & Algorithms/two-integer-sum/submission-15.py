class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            second_num = target - i
            if second_num in nums:
                second_idx = nums.index(second_num)
                if second_idx != idx:
                    res = [idx, second_idx]
                    res.sort()
                    return res
            else:
                continue
