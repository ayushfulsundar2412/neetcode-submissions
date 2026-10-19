class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Numset=set(nums)
        longest=0

        for n in nums:
            if (n-1) not in Numset:
                length=0
                while (n+length) in Numset:
                    length+=1
                longest=max(length,longest)
        return longest
            