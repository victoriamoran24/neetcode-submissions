class MinStack:

    def __init__(self):
        self.arr = []
        self.min = None
        
    def push(self, val: int) -> None:
        if self.min == None: 
            self.min = val
        if self.min > val: 
            self.min = val
        self.arr.append((val, self.min))

    def pop(self) -> None:
        if len(self.arr) == 1: 
            self.min = None
        else: 
            self.min = self.arr[len(self.arr) - 2][1]
        self.arr.pop(len(self.arr) - 1)

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]

        
