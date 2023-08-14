def main():
    arr = list(map(int, input().strip().split()))
    i = 1
    while i <= len(arr) - 1:
        elem_to_move = arr.pop(len(arr) - 1)
        for j in range(i):
            if elem_to_move < arr[j]:
                pos = 0 if j == 0 else j
                arr.insert(pos, elem_to_move)
                break
            if j == i - 1:
                arr.insert(j, elem_to_move)
        i += 1

    print(arr)


if __name__ == "__main__":
    main()
