from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree: dict[int, int]={key:0 for key in range(numCourses)}
        adj_list: dict[int, List[int]] ={key:[] for key in range(numCourses)}

        for prereq in prerequisites:
            in_degree[prereq[0]]+=1
            adj_list[prereq[1]].append(prereq[0])

        result =[]
        q = deque([])

        for key in in_degree.keys():
            if in_degree[key] == 0:
                q.append(key)
        while q:
            item = q.popleft()
            result.append(item)
            

            for neighbor in adj_list[item]:
                in_degree[neighbor] -= 1 
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    

        return result if len(result) == numCourses else []
        