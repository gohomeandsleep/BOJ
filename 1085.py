x,y,w,h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

dist = []
dist.append(x)
dist.append(w-x)
dist.append(h-y)
dist.append(y)

min_v = 1000
for i in range(4):
    if (dist[i] < min_v):
        min_v = dist[i]

print(min_v)
