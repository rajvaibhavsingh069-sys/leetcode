class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        from bisect import bisect_left, insort

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, val)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, val)

        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        return max(
            self.query(node * 2, l, mid, ql, qr),
            self.query(node * 2 + 1, mid + 1, r, ql, qr)
        )


class Solution:
    def getResults(self, queries):
        mx = max(q[1] for q in queries) + 1

        obstacles = [0, mx]

        for q in queries:
            if q[0] == 1:
                insort(obstacles, q[1])

        st = SegmentTree(mx + 1)

        for i in range(1, len(obstacles)):
            st.update(
                1,
                0,
                mx,
                obstacles[i],
                obstacles[i] - obstacles[i - 1]
            )

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                st.update(
                    1,
                    0,
                    mx,
                    right,
                    right - left
                )

                obstacles.pop(idx)

            else:
                x, sz = q[1], q[2]

                idx = bisect_left(obstacles, x + 1)

                prev = obstacles[idx - 1]

                best = st.query(
                    1,
                    0,
                    mx,
                    0,
                    prev
                )

                ans.append(best >= sz or x - prev >= sz)

        return ans[::-1]