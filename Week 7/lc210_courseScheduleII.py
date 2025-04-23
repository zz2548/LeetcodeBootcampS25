class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        prereqMap = {i:[] for i in range(numCourses)}
        for course, prereq in prereqs:
            prereqMap[course].append(prereq)

        # Visiting = all the courses we are currently visiting
        output = []
        visiting, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                # Cycle detected
                return False
            if course in visiting:
                return True
            cycle.add(course)
            for pre in prereqMap[course]:
                if dfs(pre) == False: return False
            cycle.remove(course)
            visiting.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return output
