def main():
    arr = list(map(int, input().strip().split()))
    len_arr = len(arr)
    last_elem = len_arr - 1
    for i in range(len_arr):
        j = 0
        while j < last_elem:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        last_elem -= 1
    print(arr)


if __name__ == "__main__":
    main()
