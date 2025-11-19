class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        a = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    a[i] = max(a[i],a[j]+1)
        return max(a)
        