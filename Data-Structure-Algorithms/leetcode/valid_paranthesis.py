class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        checked_values = [] 
        pairs = { ")" : "(", "]": "[", "}" : "{" }
        for c in s:
            if c in pairs:
                if checked_values and checked_values[-1] == pairs [c]: 
                    checked_values.pop()
                else:
                    return False
            else:
                pairs.append(c)
        return True if not checked_values else False

obj=Solution()
string="[{(({})}]"
result=obj.isValid(string)
print(result)