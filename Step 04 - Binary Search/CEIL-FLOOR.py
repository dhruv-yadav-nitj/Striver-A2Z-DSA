import bisect


def getFloorAndCeil(arr, n, x):
    # code here
    arr.sort()
    lower = bisect.bisect_left(arr, x)
    ans = []
    if lower < n and arr[lower] == x:
        ans.append(x)
    elif lower - 1 >= 0:
        ans.append(arr[lower - 1])
    else:
        ans.append(-1)
    upper = bisect.bisect_right(arr, x)
    if upper < n:
        if upper - 1 >= 0 and arr[upper - 1] == x:
            ans.append(x)
        else:
            ans.append(arr[upper])
    else:
        ans.append(-1)
    return ans
