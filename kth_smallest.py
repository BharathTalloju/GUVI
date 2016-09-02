try:
    arr = map(int, raw_input().strip().split())
    k = int(raw_input().strip())
except (ValueError, TypeError):
    print "Invalid"
    exit(1)

arr.sort()
if (k > len(arr)) or k < 1:
    print None
print arr[-k]
