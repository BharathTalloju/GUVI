try:
    arr = map(int, raw_input().strip().split())
except (TypeError, ValueError):
    print "Invalid"
    exit(1)
    pass
arr = list(set(arr))
arr.sort(reverse=True)
result = ''
for c in arr:
    result += str(c)
print result
