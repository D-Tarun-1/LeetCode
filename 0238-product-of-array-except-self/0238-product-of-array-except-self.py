class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dummy = nums
        ans = [0]*len(nums)
        mul = 1
        for i in nums:
            mul *= i
        if(mul == 0):
            check = 0
            for i in range(0, len(nums)):
                if(nums[i] == 0):
                    check = i
            dummy[check] = 1
            mul1 = 1
            for i in nums:
                mul1 *= i
            ans[check] = mul1
        else:
            for i in range(len(nums)):
                ans[i] = (mul//nums[i])
        return ans
        