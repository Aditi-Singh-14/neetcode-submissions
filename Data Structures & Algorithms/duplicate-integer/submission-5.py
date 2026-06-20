class Solution:
    def hasDuplicate(self, nums):
        num=set(nums)
        a=len(nums)
        b=len(num)
        if a==b:
            return False
        else:
            return True