"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Input: nums = [1,2,3,1]
    Output: true
    otherwise: false
"""

class Duplication:
    def containDuplication(self,nums:list[int])-> bool:
        #sort the list first
        nums.sort()
        for index in range(len(nums)-1):
            if nums[index] == nums[index + 1]:
                return True
        return False
duplication_obj =Duplication()
values =[2,3,4,5,3]
duplicate_or_not = duplication_obj.containDuplication(nums = values)
if duplicate_or_not:
    print(f"The list conatine duplicate values.")
else:
    print(f"The didn't contain duplicate values.")

#another way to solve this. using hashmap
class Solution:
    def avoidDuplication(numbers: list[int])->bool:
        #here create new memory to check the values are duplicated or not
        hashSet = set()
        for value in numbers:
            if value in hashSet:
                return True
            hashSet.add(value)
        return False
    #time O(n)  space O(n)