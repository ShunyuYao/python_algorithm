def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    mid_val = arr[0]
    below = [x for x in arr[1:] if x < mid_val]
    above = [x for x in arr[1:] if x > mid_val]
    return quick_sort(below) + [mid_val] + quick_sort(above)

if __name__ == '__main__':
    print(quick_sort([2, 4, 1, 3, 12, 5, 3, 4]))
