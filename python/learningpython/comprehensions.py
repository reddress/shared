def evenp(x):
    return x % 2 == 0

[1 if evenp(n) else 0 for n in [1,2,3,4,5]]
[1 if evenp(n) else 0 for n in [1,2,3,4,5] if evenp(n)]

(lambda x: 1 if not evenp(x) else 0)(2)

[x + y for x in "ABC" for y in "1234" if int(y) > 1]

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
N = [[2,2,2],
     [3,3,3],
     [4,4,4]]

[row[1] for row in M]  # column 2
[M[i][i] for i in range(len(M))]  # diagonal
[M[i][len(M)-1-i] for i in range(len(M))]  # other diagonal

[col + 10 for row in M for col in row]
[[col + 10 for col in row] for row in M]

[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]

[[col1 * col2 for (col1,col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]

list(zip(M, N))
