def findJudge(N, trust):
    m = [0] * 1000
    for i, j in trust: m[i-1], m[j-1] = -1, m[j-1] + 1
    maxv = max(m)
    return m.index(maxv) + 1 if maxv == N-1 else -1
