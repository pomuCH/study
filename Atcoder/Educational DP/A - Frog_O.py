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
h = list(map(int,input().split()))

H1 = abs(h[0] - h[1])
H2 = abs(h[0] - h[2])

dp = [0] * n

if H1 > H2:
  dp[0] = H2
  i = 2
elif H1 < H2:
  dp[0] = H1
  i = 1
elif H1 == H2:
  dp[0] = 0
  i = 2

j = 1
while True:
  h1 = abs(h[i] - h[i + 1])
  h2 = abs(h[i] - h[i + 2])
  if h1  > h2:
    dp[j] = dp[j - 1] + h2
    i += 2
  elif h1 < h2:
    dp[j] = dp[j - 1] + h1
    i += 1
  elif h1 == h2:
    i += 2
  j += 1
  if i >(n -2):
    break
print(dp[-1])
