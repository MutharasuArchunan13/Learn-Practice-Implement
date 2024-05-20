import operator
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
}
        operand=[]
        cals=None
        if len(tokens)==1:
            return int(tokens[0])
        for val in tokens:
            try:
                value=int(val)
                operand.append(value)     
            except ValueError:
                val1=operand.pop()
                val2=operand.pop()
                cals =int(operators[val](val2,val1))
                operand.append(cals)

        return cals
            
tokens=["2","1","+","3","*"]
result=ReverPolishNotion().evalRPN(tokens)
print(result)