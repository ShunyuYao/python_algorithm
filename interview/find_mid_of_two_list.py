"""
假设有两个有序数组arr1和arr2，求出arr1和arr2合并后的中位数
"""
# to do: 代码不够简洁
even_mid = []
def cal_mid(even, k, total_len, temp):
    if even:
        if k == total_len // 2 - 1:
            even_mid.append(temp)
        if k == total_len // 2:
            return (even_mid[0] + temp) / 2
    else:
        if k == total_len // 2:
            return temp
    return None

def find_mid_of_two_arr(arr1, arr2):
    i = j = k = 0
    total_len = len(arr1) + len(arr2)
    even = total_len % 2 == 0
    even_mid = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            temp = arr1[i]
            i += 1
        else:
            temp = arr2[j]
            j += 1
        result = cal_mid(even, k, total_len, temp)
        if result:
            return result
        k += 1

    while i < len(arr1):
        temp = arr1[i]
        i += 1
        result = cal_mid(even, k, total_len, temp)
        if result:
            return result
        k += 1

    while j < len(arr2):
        temp = arr2[j]
        j += 1
        result = cal_mid(even, k, total_len, temp)
        if result:
            return result
        k += 1

    return []

if __name__ == '__main__':
    arr1 = [1, 3, 12, 20]
    arr2 = [2, 6, 7, 15]

    arr3 = [1, 3, 9]
    arr4 = [1, 4]
    mid = find_mid_of_two_arr([2,5], [2,7])
    # [1, 2, 3, 6, 7, 12, 15, 20]
    print(mid)

"""
思路： 因为数组有序，合并不妨当作归并排序的“并”阶段。
而且无需全部排列，排到一般就可以直到其中位数了
中位数：偶数个是中间两个数的平均值，奇数个就是中间的值
"""
