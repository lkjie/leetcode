# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
#
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#
# arr = [12,42,4,5,1,3,6,7]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i]),



def partitioin(arr,low,high):
    aim = arr[high]
    pi = low-1
    for i in range(low, high):
        if arr[i] < aim:
            pi+=1
            arr[pi],arr[i] = arr[i],arr[pi]
    arr[pi+1],arr[high] = arr[high], arr[pi+1]
    return pi+1

def qsort(arr,low,high):
    if low < high:
        mid = partitioin(arr,low,high)
        qsort(arr,low,mid-1)
        qsort(arr,mid+1,high)

l = [12,42,4,5,1,3,6,7,1]
qsort(l, 0, len(l)-1)
print(l)