def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        temp=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],temp+nums[i])
            maxi=max(temp,maxi)
        return maxi
