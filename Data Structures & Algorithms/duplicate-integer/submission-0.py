class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = []
        for i in nums:
            if i not in present:
                present.append(i)
            else:
                break
        if len(present) == len(nums):
            return False
        else:
            return True
