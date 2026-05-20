from collections import deque, Counter
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        task_heap =[(-1 * cnt) for cnt in count.values()]
        heapify(task_heap)

        task_q = deque([])

        time = 0
        while task_heap or task_q:
            time += 1
            if len(task_heap) > 0:
                cnt = 1 + heappop(task_heap)
                if cnt < 0:
                    task_q.append([cnt, time + n])
            while len(task_q) > 0 and task_q[0][1] <= time:
                task = task_q.popleft()
                heappush(task_heap, task[0])
        return time 
