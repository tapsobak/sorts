a = [5, 3, 8, 6, 2]


def sorting(a_list):
    n = len(a_list)
    for j in range(n):
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                temp0 = a_list[i]
                temp1 = a_list[i + 1]
                a_list[i] = temp1
                a_list[i + 1] = temp0

    return a_list


if __name__ == "__main__":
    print(sorting(a))
