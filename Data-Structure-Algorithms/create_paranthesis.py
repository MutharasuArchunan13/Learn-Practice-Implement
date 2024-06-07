from typing import List
# def generateParenthesis(self, n: int) -> List[str]:
# 	def dfs(left, right, s):
# 		if len(s) == n * 2:
# 			res.append(s)
# 			return 

# 		if left < n:
# 			dfs(left + 1, right, s + '(')

# 		if right < left:
# 			dfs(left, right + 1, s + ')')

# 	res = []
# 	dfs(0, 0, '')
# 	return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def paran(left,right):
            if left==right==n:
                res.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                paran(left+1,right)
                stack.pop()
            if right < left:
                stack.append(")")
                paran(left,right+1)
                stack.pop()
        paran(0,0)
        return res
        
Solution().generateParenthesis(2)
values=[]
for val in enumerate(values):
    print(val)