from typing import List

class Solution:
    """
    algorithm:
    1.we have find the largest sequence in list so first we 
      find the small number in sequence.if the no element smaller than current element is present
    2.Then count the number of elements in sequence
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_consecutive = 0

        for num in num_set:
            if num - 1 not in num_set:  
                current_num = num
                current_length = 1

                while current_num + 1 in num_set: 
                    current_num += 1
                    current_length += 1

                longest_consecutive = max(longest_consecutive, current_length)

        return longest_consecutive
                
obj = Solution()
input1 =[1,2,3,6,7,9,10,11,12]
result = obj.longestConsecutive(input1)
print(result)