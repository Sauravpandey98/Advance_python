def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    print(binary_search(arr, target))


if __name__ == "__main__":
    main()
