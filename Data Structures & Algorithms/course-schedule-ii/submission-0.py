class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1

        sources = deque()
        for node, degree in inDegree.items():
            if degree == 0:
                sources.append(node)


        courses = []
        while sources:
            node = sources.popleft()
            courses.append(node)

            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    sources.append(neighbor)

        if len(courses) == numCourses:
            return courses
        return []