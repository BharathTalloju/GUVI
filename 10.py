try:
    arr1= map(int, raw_input().strip().split())
    arr2 = map(int, raw_input().strip().split())
except:
    print "Invalid input"
    exit(1)
    pass
arr1 = set(arr1)
arr2 = set(arr2)
if len(arr1 - arr2) == 0:
    print True
    pass
else:
    print False
