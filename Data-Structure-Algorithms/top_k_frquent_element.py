from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = {}
        result = []
        for num in nums:
            if num in frequent_dict:
                frequent_dict[num] +=1
            else:
                frequent_dict[num] = 1
        sorted_dict = sorted(frequent_dict.items(), key=lambda x: x[1], reverse=True)

        
class_obj = Solution()
class_obj.topKFrequent([1,1,1,1,2,2,3,3,3],2)