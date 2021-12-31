# This code is using Mid-pivot Quick Sort. You can use Merge Sort or any other accepted Sorting Algorithms if you want

n = int(input())
arr = list(map(int, input().split()))

def quick_sort(arr, start_point, end_point):
    mid_element = arr[(start_point + end_point) // 2]
    i = start_point
    j = end_point
    
    while i <= j:
        while arr[i] < mid_element: i += 1
        while arr[j] > mid_element: j -= 1
        
        if i <= j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            i += 1
            j -= 1

    if start_point < j: quick_sort(arr, start_point, j)
    if i < end_point: quick_sort(arr, i, end_point)

quick_sort(arr, 0, n - 1)

for i in arr:
    print(i, end = " ")