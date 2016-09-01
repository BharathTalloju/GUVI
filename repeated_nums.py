try:
    arr = map(int,raw_input().strip().split())
except (TypeError, ValueError):
    print "Invalid Inputs"
    exit(1)
arr.sort()
n = len(arr)
if n == 1:
    pass
else:
    result = ''
    i,j = 0,1
    while j<n:
        if arr[i] < 0:
            print '0'
            exit(1)
        if arr[i] == arr[j]:
            result += str(arr[i])+' '
            while  j < n and arr[i] == arr[j]:
                j += 1
                pass
            i = j
            j += 1
            pass
        else:
            i += 1
            j += 1
    print result
