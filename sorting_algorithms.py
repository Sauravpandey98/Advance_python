from typing import List
import math


def bubble_sort(arr: List[int]):
    """
    Time Complexity :
        Average: O(n^2)
        Best: O(n)
    Space: O(1)
    * In space time complexity
    * It is stable sorting algorithm.That is mantain the relative order of same elements
    """
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break


def selection_sort(arr: List[int]):
    """
    Time Complexity: O(n^2)
        Average: O(n^2)
        Best: O(1)
    Space: O(1)
    * It is not stable
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr: List[int]):
    """
    Time Complexity:
        O(nlogn)
    Space: O(n)
    * It is a stable algorithm
    """
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge them
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = left[j]
        j += 1
        k += 1

    return arr


def quick_sort(arr: List[int], low: int, high: int):
    """
    Average: O(nlogn)
    Worst: O(n^2)
    Space: O(1)
    """

    def get_partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = get_partition(low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
