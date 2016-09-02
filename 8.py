try:
    arr = map(int, raw_input().strip().split())
except (ValueError, TypeError):
    print "Invalid"
    exit(1)
    pass
arr.sort()
n = len(arr)
none_flag = True
for pivot in xrange(n-1, 0, -1):
    i, j = 0, pivot
    while i<j:
        if arr[i] + arr[j] == arr[pivot]:
            print arr[i],arr[j],arr[pivot]
            i+=1
            j-=1
            none_flag=False
            pass
        elif arr[i] + arr[j] < arr[pivot]:
            i+=1
            pass
        else:
            j-=1
            pass
if none_flag :
    print "None"
