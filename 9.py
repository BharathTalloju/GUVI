try:
    arr_org = map(int, raw_input().strip().split())
except (ValueError, TypeError):
    print "Invalid"
    exit(1)
    pass
arr = sorted(arr_org)
n=len(arr)
i = 0
while arr[i] < 0:
    i+=1
    pass
np = i-1
pp = i
min = (9999999, None, None)
while np >=0 and pp < n:
    new_min = arr[pp]+arr[np]
    if abs(new_min) < min:
        min = (abs(new_min), arr[np], arr[pp])
        pass
    if new_min > 0:
        np-=1
        continue
    if new_min < 0:
        pp+=1
        continue
    if new_min == 0:
        break

if min[1] is not None:
    print arr_org.index(min[1]), arr_org.index(min[2])
else:
    print "None"

