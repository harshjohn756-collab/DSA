class Solution(object):
    def sortArray(self, nums):
        for i in range(1,len(nums)):
            current = nums[i]
            j= i-1
            while j>=0 and nums[j]>current:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1]= current
        print(nums)
sc = Solution()
sc.sortArray([5,1,1,2,0,0])
