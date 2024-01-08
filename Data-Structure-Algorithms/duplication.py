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