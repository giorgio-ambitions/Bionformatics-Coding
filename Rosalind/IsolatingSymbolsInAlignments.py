def score(a, b):
    return 1 if a == b else -1
def score(a, b):
    return 1 if a == b else -1

def solve(s, t):
    m = len(s)
    n = len(t)

    # Forward DP:
    # dp[i][j] = best global alignment score of
    # s[:i] and t[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = -i

    for j in range(1, n + 1):
        dp[0][j] = -j

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(
                dp[i - 1][j - 1] + score(s[i-1],t[j-1]),
                dp[i - 1][j] - 1,
                dp[i][j - 1] - 1
        )

    # Backward DP:
    # rev[i][j] = best global alignment score of
    # s[i:] and t[j:]
    rev = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        rev[i][n] = -(m - i)

    for j in range(n - 1, -1, -1):
        rev[m][j] = -(n - j)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            rev[i][j] = max(
                rev[i + 1][j + 1] +  score(s[i], t[j]),
                rev[i + 1][j] - 1,
                rev[i][j + 1] - 1
            )

    # Calculate sum of M
    total = 0

    for i in range(m):
        for j in range(n):
            M_ij = (
                dp[i][j]
                + score(s[i], t[j])
                + rev[i + 1][j + 1]
            )

            total += M_ij

    return dp[m][n], total


# Example
s = "ATAGATA"
t = "ACAGGTA"

answer1, answer2 = solve(s, t)

print(answer1)
print(answer2) 
