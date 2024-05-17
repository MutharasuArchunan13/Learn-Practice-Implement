import operator
from typing import List

class ReverPolishNotion:

    def calculate(self, values: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
}
        left_operand=[]
        right_operand=[]
        cals=""
        operator_stat=False
        for val in values:
            try:
                value=int(val)
                if not operator_stat:
                    left_operand.append(value)
                else:
                    right_operand.append(value)     
            except ValueError:
                operator_stat=True
                if right_operand and cals:
                    cals =operators[val](cals,right_operand.pop())
                elif left_operand:
                    if not cals:
                        val_1=left_operand.pop()
                        val_2=left_operand.pop()
                        cals =operators[val](val_2,val_1)
                    else:
                        cals =operators[val](left_operand.pop(),cals)
        return round(cals)
            
tokens=["4","13","5","/","+"]
result=ReverPolishNotion().calculate(tokens)
print(result)