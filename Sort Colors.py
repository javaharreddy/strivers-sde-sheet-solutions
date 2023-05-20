def sortColors(self, nums: List[int]) -> None:
        low,high,mid=0,len(nums)-1,0
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
