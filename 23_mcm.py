def mcm(i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    ans = float('inf')

    for k in range(i, j):
        cost =(
            mcm(i,k,dp),
            mcm(k+1,j,dp),
            arr[i-1]*arr[k]*arr[j]
        )

    dp[i][j] = ans
    return ans


arr = [10, 30, 5, 60]
n = len(arr)
dp = [[-1]*n for _ in range(n)]

print(mcm(1, n-1))  
