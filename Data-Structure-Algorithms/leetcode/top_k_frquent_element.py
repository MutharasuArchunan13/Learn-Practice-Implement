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
        sorted_dict = dict(sorted(frequent_dict.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)
        #must return the top k elements only
        count = 0
        for key,value in sorted_dict.items():
            result.append(key)
            count +=1
            if count == k:
                break
        
        return result



        
class_obj = Solution()
result = class_obj.topKFrequent([1,1,1,1,2,2,3,3,3,3,3,3,3],2)
print(f"The top k frequent elements: {result}")