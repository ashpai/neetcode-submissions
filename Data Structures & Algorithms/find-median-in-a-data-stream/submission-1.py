from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        # self.count: int  = 0
        # self.median: float = float('-inf')
        # self.elements: List[int] = []
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # # add number
        # self.elements.append(num) # o(1) 

        # # update count 
        # self.count += 1 # o(1)

        # temp, no_pops = [], (self.count - 1)  // 2 if self.count % 2  == 0 else self.count  // 2 
        # # calculate median
        # heapify(self.elements) #o(log(n))

        # for _ in range(no_pops):
        #     temp.append(heappop(self.elements))
        
        # if self.count % 2  == 0:
        #     num1, num2 = heappop(self.elements), heappop(self.elements)
        #     self.median = (num1 + num2) / 2
        #     temp.append(num1)
        #     temp.append(num2)
        # else:
        #     num1= heappop(self.elements)
        #     self.median = num1
        #     temp.append(num1)
        
        # while temp:
        #     self.elements.append(temp.pop())
        # small - max heap
        # large - min heap
        heappush(self.small, -1 * num)

        #balancing
        # 1. top of max heap <= top of min heap 

        if self.large and self.small and ((-1 * self.small[0]) > self.large[0]):
            heappush(self.large, -1 * heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heappush(self.small, -1 * heappop(self.large))
        


        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2 
        
        
        