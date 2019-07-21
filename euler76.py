
w, h = 105, 105;
dp = [[0 for x in range(w)] for y in range(h)]
def recurse(n , maxpart):
    sum  = 0

    for i in range(1, min(n+1 ,maxpart+1)):

        if(dp[n-i][i] != 0):
            sum += dp[n-i][i]
        else:
            sum += recurse(n - i, i)
    dp[n][maxpart] = sum
    return sum

for i in range(101):
    dp[0][i] = 1

ans = recurse(100,100)
print(ans)



sum = 0
for i in range(1,101):
    sum += dp[100][i]
print(sum)


# 
# dp2 = [0]*101
# dp2[2] = 1
# for i in range(3, 101):
#     for j in range(1, i):
#         dp2[i] += dp2[j]
#
# print(dp2[100])
