from typing import List
class Solution:
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
        