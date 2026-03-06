a = [5, 3, 8, 6, 2]
b = [7, 2, 8, 1, 5]


def sorting(a_list):
    n = len(a_list)
    for j in range(
        n
    ):  # nested loop is required to cover every element in the list to make sure the whole list is sorted.
        for i in range(n - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = (
                    a_list[i + 1],
                    a_list[i],
                )  # pythonic way to swap between elements in positions i and i + 1.

    return f"Sorted list: {a_list}"


if __name__ == "__main__":
    print(sorting(a))
    print(sorting(b))
