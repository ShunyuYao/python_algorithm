def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_list = alist[:mid]
        right_list = alist[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                alist[k] = left_list[i]
                i += 1
            else:
                alist[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            alist[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            alist[k] = right_list[j]
            j += 1
            k += 1

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    merge_sort(alist)
    print(alist)
