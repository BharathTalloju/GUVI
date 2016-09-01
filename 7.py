#hell no
try:
    arr = map(int, raw_input().strip().split())
except (TypeError, ValueError):
    print "Invalid"
    exit(1)
    pass
r = 0
for i in arr:
    r ^= i
    pass
print r
