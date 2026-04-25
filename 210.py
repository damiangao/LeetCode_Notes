class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        indegs = [0] * numCourses
        q = deque()
        ret = []

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indegs[info[0]] += 1
        
        for i, x in enumerate(indegs):
            if not x:
                q.append(i)
        
        while q:
            cur = q.pop()
            ret.append(cur)

            for k in edges[cur]:
                indegs[k] -= 1
                if not indegs[k]:
                    q.append(k)
        if len(ret) < numCourses:
            return []
        return ret
