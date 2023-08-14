def main():
    arr = list(map(int, input().strip().split()))
    len_arr = len(arr)
    last_elem = len_arr - 1
    for i in range(len_arr):
        max_elem = arr[0], 0
        j = 0
        while j <= last_elem:
            if arr[j] > max_elem[0]:
                max_elem = arr[j], j
            if j == last_elem:
                arr[max_elem[1]], arr[last_elem] = arr[last_elem], arr[max_elem[1]]
            j += 1
        last_elem -= 1
    print(arr)


if __name__ == "__main__":
    main()
