def mergesort(arr):
    print(arr) #print
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    l = r = 0
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l = l+1
        else:
            res.append(right[r])
            r = r+1
    res.extend(left[l:])
    res.extend(right[r:])
    print(res) #print
    return res


print(mergesort([9,8,7,6,5]))


