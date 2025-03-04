def findZigZagSequence(a, n):
    # Sorting the array
    a.sort()
    
    # Find the mid element
    mid = int(n//2)
    
    # Swap the last element of the sorted array (highest) wit the mid elem.
    a[mid], a[n-1] = a[n-1], a[mid]

    # Using left and right pointers from [mid+1, end-2] to swap the elements on the left and right
    st = mid + 1
    ed = n - 2
    while(st < ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
            
    return
