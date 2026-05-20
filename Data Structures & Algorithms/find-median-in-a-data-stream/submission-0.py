from heapq import heapify, heappop
class MedianFinder:

    def __init__(self):
        self.count: int  = 0
        self.median: float = float('-inf')
        self.elements: List[int] = []
        

    def addNum(self, num: int) -> None:
        # add number
        self.elements.append(num) # o(1) 

        # update count 
        self.count += 1 # o(1)

        temp, no_pops = [], (self.count - 1)  // 2 if self.count % 2  == 0 else self.count  // 2 
        # calculate median
        heapify(self.elements) #o(log(n))

        for _ in range(no_pops):
            temp.append(heappop(self.elements))
        
        if self.count % 2  == 0:
            num1, num2 = heappop(self.elements), heappop(self.elements)
            self.median = (num1 + num2) / 2
            temp.append(num1)
            temp.append(num2)
        else:
            num1= heappop(self.elements)
            self.median = num1
            temp.append(num1)
        
        while temp:
            self.elements.append(temp.pop())

        

    def findMedian(self) -> float:
        return self.median
        
        