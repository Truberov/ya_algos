def main():
    arr = list(map(int, input().strip().split()))
    arr_2 = []

    for _ in range(len(arr)):
        elem_to_move = arr.pop()
        for i in range(len(arr_2)):
            if elem_to_move < arr_2[i]:
                arr_2.insert(i, elem_to_move)
                break
            if i == len(arr_2) - 1:
                arr_2.insert(i + 1, elem_to_move)
        if len(arr_2) == 0:
            arr_2.insert(-1, elem_to_move)

    print(arr_2)


if __name__ == "__main__":
    main()
