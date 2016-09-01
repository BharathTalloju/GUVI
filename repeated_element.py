try:
    arr = map(int, raw_input().strip().split())
except (ValueError):
    print "invalid"
    exit(1)
    pass
visited = set()

for i in arr:
    if i in visited:
        print i
        break
    visited.add(i)

