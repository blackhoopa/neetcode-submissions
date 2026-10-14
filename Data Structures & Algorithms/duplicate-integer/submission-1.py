class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = set()
        for i in nums:
            if i not in present:
                present.add(i)
            else:
                break
        if len(present) == len(nums):
            return False
        else:
            return True
