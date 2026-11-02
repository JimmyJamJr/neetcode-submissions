class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        # for each row of mat2, keep only its nonzero entries as (column, value)
        nz2 = [[(j, v) for j, v in enumerate(row) if v != 0] for row in mat2]

        result = [[0] * n for _ in range(m)]
        for i in range(m):                    # build result row i
            for p in range(k):                # walk along mat1 row i
                a = mat1[i][p]
                if a == 0:
                    continue                  # zero weight: skip row p of mat2 entirely
                for j, v in nz2[p]:           # only nonzeros of mat2 row p
                    result[i][j] += a * v
        return result