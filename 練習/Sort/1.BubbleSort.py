def bubble_sort(arr):
    loop_size = len(arr) - 1
    for i in range(loop_size):
        for j in range(loop_size):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr1 = [1, 6, 2, 7, 9, 0]
print(bubble_sort(arr1))


# def bubble_sort(data):
#     length = len(data)
#     # 要素の位置を確定させる操作を(length-1)回行う
#     for i in range(1, length):
#         # いちばん左端の要素から順に「左右を比較して入れ替える」操作を繰り返す
#         for j in range(0, length - i):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#         # いちばん右端の要素から順に位置が確定していく


# if __name__ == "__main__":
#     data = [3, 8, 1, 2, -1, -10, 4, 2]
#     bubble_sort(data)
#     print(data)


# # whileループを使ったバブルソート
# def bubble_sort2(arr):
#     length = len(arr)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(1, length):
#             if arr[i - 1] > arr[i]:
#                 arr[i - 1], arr[i] = arr[i], arr[i - 1]
#                 swapped = True
#     return arr


# # arr1 = [8, 9, 6, 2, 5, 1, 4]

# # print(bubble_sort(arr1))

# # 練習


# def bubble_sort3(arr):
#     length = len(arr)
#     for i in range(1, length):
#         for j in range(0, length - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# if __name__ == "__main__":
#     arr3 = [2, 9, -2, 0, 6, 7, 11]
#     bubble_sort(arr3)
