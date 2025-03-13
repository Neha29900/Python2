class Solution(object):
    def removeDuplicates(self, nums):
        
        if not nums:
            return 0

        # Pointer for the unique elements
        unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        return unique_index + 1  # The length of the unique elements list
