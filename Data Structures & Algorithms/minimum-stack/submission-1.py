class MinStack:
    """
    ["MinStack", "push", -2, "push", -2, "push", -3, "push", -3, "getMin", "pop", "getMin"]
    main=[1, 2]
    min=[1]
    """
    def __init__(self):
        self.main_stack = []
        self.min_stack =[]
    

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.main_stack) == 0:
            return
        popped = self.main_stack.pop()

        if self.min_stack[-1] == popped:
            self.min_stack.pop()
        
        

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
