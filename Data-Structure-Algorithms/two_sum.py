class TwoSum :
    """
        we receive a list of integer value defintely add any two values we got the 
        target so return that two values index in our list
    """
    def returnTwoSumInsex(self,nums:list[int],target:int):
        length = len(nums)
        for index in range(length):
            for index2 in range(index+1,length):
                if nums[index] + nums[index2] == target:
                    return [index,index2]
        return
#but this is leads to O(n^2) so here we try another logic
    
    def returnTwoSumIndexSolution2(self,nums: list[int],target:int):
        for index in range(len(nums)):
            temp = target - nums[index]
            if temp in nums:
                return [index,nums.index(temp)]
        return

val =TwoSum()
result = val.returnTwoSumIndexSolution2([2,4,5,6,9],10)
result = val.returnTwoSumInsex([2,4,5,6,9],10)
print(f'The two_sum index are: {result}')