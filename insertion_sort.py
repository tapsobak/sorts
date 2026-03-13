a = [5, 3, 8, 6, 2]
b = [7, 2, 8, 1, 5]
c = [3, 1, 2]
d = [3]
e = []


def insert_sorting(a_list):
    n = len(a_list)
    for i in range(n):
        for j in range(n - 1):
            if a_list[j] > a_list[j + 1]:
                temp1 = a_list[j + 1]
                a_list.pop(j + 1)
                a_list.insert(j, temp1)

    return a_list


if __name__ == "__main__":
    print(insert_sorting(a))
    print(insert_sorting(b))
    print(insert_sorting(c))
    print(insert_sorting(d))
    print(insert_sorting(e))
