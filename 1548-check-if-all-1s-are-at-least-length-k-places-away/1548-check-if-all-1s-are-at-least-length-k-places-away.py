class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums)):
            if nums[i]==1:
                for j in range(i+1,min(i+k+1,len(nums))):
                    if nums[j]==1:
                        return False
        return True