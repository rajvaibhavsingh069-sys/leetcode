class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        front = {0}
        back = {n - 1}

        visited = {0, n - 1}

        steps = 0

        while front:

            # always expand smaller side
            if len(front) > len(back):
                front, back = back, front

            nxt = set()

            for i in front:

                if i in back:
                    return steps

                neighbors = graph[arr[i]] + [i - 1, i + 1]

                for nei in neighbors:
                    if 0 <= nei < n:

                        if nei in back:
                            return steps + 1

                        if nei not in visited:
                            visited.add(nei)
                            nxt.add(nei)

                graph[arr[i]].clear()

            front = nxt
            steps += 1