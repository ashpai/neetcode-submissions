class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operate(operator, num_1, num_2):
            if operator == "-":
                return num_1 - num_2
            if operator == "+":
                return num_1 + num_2
            if operator == "*":
                return num_1 * num_2
            else:
                return int(num_1 / num_2)
        eval_stack = []

        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                eval_stack.append(int(tokens[i]))
            else:
                num_2 = eval_stack.pop()
                num_1 = eval_stack.pop()
                eval_stack.append(operate(tokens[i],num_1, num_2))
        
        return eval_stack[0]


        