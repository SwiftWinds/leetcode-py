from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points_set = set([tuple(x) for x in points])

        def dot(p1, p2):
            return p1[0] * p2[0] + p1[1] * p2[1]

        def sub(p1, p2):
            return [p1[0] - p2[0], p1[1] - p2[1]]

        def add(p1, p2):
            return [p1[0] + p2[0], p1[1] + p2[1]]

        def area(u, v):
            return abs(u[0] * v[1] - v[0] * u[1])

        min = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    vec1 = sub(points[j], points[i])
                    vec2 = sub(points[k], points[i])
                    if dot(vec1, vec2) == 0:
                        vec3 = add(points[i], add(vec1, vec2))
                        if tuple(vec3) in points_set:
                            a = area(vec1, vec2)
                            if min is None or a < min:
                                min = a
        if min is None:
            return 0
        return min
