n = int(input())
h = list(map(int,input().split()))
result = 0
i = 0
while(i <= (n - 2)):
  h1 = abs(h[i] - h[i + 1])
  h2 = abs(h[i] - h[i + 2])
  if h1  > h2:
    result += h2
    i += 2
  elif h1 < h2:
    result += h1
    i += 1
  elif h1 == h2:
    if (i + 4)<= (n - 2):
      h3 = abs(h[i + 1] - h[i + 2])
      h4 = abs(h[i + 1] - h[i + 3])
      h5 = abs(h[i + 2] - h[i + 3])
      h6 = abs(h[i + 2] - h[i + 4])
      
      if h3 > h5 or h4 > h5 or h3 > h6 or h4 > h6:
        i += 2
      else:
        i += 1
print(result)
