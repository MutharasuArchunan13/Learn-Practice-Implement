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
#but this is leads two O(n^2) so here we try another logic