
from collections import defaultdict

class GroupAnagram:
    """
        use one default dict list inside that list key as sorted string then their 
        values are list
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)

        result = list(anagram_groups.values())
        return result

obj = GroupAnagram()
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat","",""]
result = obj.groupAnagrams(input_strs)
print(result)
