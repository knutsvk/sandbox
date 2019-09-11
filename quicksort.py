def quicksort(input_arr):
    """
    Quicksort algorithm
    Returns the sorted array. 
    """
    arr = input_arr[:]
    n = len(arr)
    if n < 2:
        return arr

    pivot = n-1
    checker = 0
    while checker < pivot:
        if arr[checker] < arr[pivot]:
            checker += 1
        else:
            if pivot - checker == 1:
                tmp = arr[pivot]
            else:
                tmp = arr[pivot-1]
                arr[pivot-1] = arr[pivot]
            arr[pivot] = arr[checker]
            arr[checker] = tmp
            pivot -= 1

    return quicksort(arr[:pivot]) + [arr[pivot]] + quicksort(arr[pivot+1:])


if __name__ == "__main__":
    arr = [2, -100, 0, 3, 7, 8, 0, 5, 2, 1, 9, 5, 4, 0, -4, 0, 0, 0]
    res = quicksort(arr)
    print(arr)
    print(res)
