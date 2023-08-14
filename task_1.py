def main():
    arr = list(map(int, input().strip().split()))
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


if __name__ == "__main__":
    main()
