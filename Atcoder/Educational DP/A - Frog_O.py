'''
i段目にくる方法を考える

i段目に到達する方法は、i-1段目から1段上ってくるか、i-2段目から2段上ってくるかの2通りのみ
dp[i] = dp[i - 1] + dp[i - 2] ->漸化式

dp[i] = i段目までの上り方の数として、

i      0 1 2 3 4 5 6
dp[i]  1 1 2 3 5 8 13

dp[0] = 1(出発地点。何もしない1通り)
dp[1] = 1 (1段上るだけの１通り)
dp[2] = dp[1] + dp[0] = 1 + 1 = 2
dp[3] = dp[2] + dp[1] = 2 + 1 = 3
dp[4] = dp[3] + dp[2] = 3 + 2 = 5
dp[5] = dp[4] + dp[3] = 5 + 3 = 8
dp[6] = dp[5] + dp[4] = 8 + 5 = 13

dp [i] = dp[i - 1] + max(h)?
'''
n = int(input())
h = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

dp = [0] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])

i = 2
while i < n:
    dp[i] = min(
        dp[i-1] + abs(h[i]-h[i-1]),
        dp[i-2] + abs(h[i]-h[i-2])
    )
    i += 1

print(dp[-1])
