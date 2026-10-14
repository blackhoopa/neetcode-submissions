class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        for x in range(len(nums)):
            first = nums[x]
            b = x    
            while b != len(nums)-1:
                a = b + 1
                sum = first + nums[a]
                if sum == target:
                   return [x,a]
                b+=1
