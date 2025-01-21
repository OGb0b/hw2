def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        while arr[mid] == None:
            mid += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            while arr[mid-1]== None:
                mid -= 1
            right = mid - 1

    return -1


