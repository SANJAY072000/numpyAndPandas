lst = list(map(int, input().split()))
f = 1
for i in range(1, lst[1]+1):
    f = i * lst[0]
    print("%d x %d = %d" % (lst[0], i, f))


