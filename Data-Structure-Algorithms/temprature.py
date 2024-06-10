from typing import List
class Solution:
    """
    In this solution time complexity is O(N)
    why because once i travel in the list only 1 iteration is required.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for index,temp in enumerate(temperatures):
            i=index+1
            iteration=1
            while i<len(temperatures):
                if temp<temperatures[i]:
                    result[index]=iteration
                    break
                i+=1
                iteration+=1
        return result
        

result=Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
print(result)