

from typing import List
from functools import reduce

class ProductOfArray:
    def productExceptSelf(self,nums : List[int]) -> List[int]:
        result = []
        for index in range(len(nums)):
            temp = nums.copy()
            temp.pop(index)
            result.append(reduce(lambda x,y: x*y,temp))
        return result

obj = ProductOfArray().productExceptSelf([1,2,3,4])
print(obj)