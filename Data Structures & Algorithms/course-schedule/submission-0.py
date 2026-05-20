class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {course: 0 for course in range(numCourses)}
        adj_list = {course:[] for course in range(numCourses)}

        for pr in prerequisites:
            in_degree[pr[0]] += 1
            adj_list[pr[1]].append(pr[0])
        
        q = deque([])
        seen = set()

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
                seen.add(course)
        

        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for neighbor in adj_list[course]:
                if neighbor not in seen:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
                        seen.add(neighbor)
        

        return len(order) == numCourses

        