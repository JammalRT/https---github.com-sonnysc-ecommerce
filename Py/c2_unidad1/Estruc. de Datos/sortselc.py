def select_sort(arr):
    n = len(arr)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[minimo]:
                minimo = j 
        arr[i], arr[minimo] = arr[minimo], arr[i]
        print(arr)
    return arr
       
arr = [90, 34, 20, 12, 30, 11, 100]
select_sort(arr)