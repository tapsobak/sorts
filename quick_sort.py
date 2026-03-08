a = [5, 3, 8, 6, 2]
b = [7, 2, 8, 1, 5]
c = [3]
d = []


def quick_sorting(a_list):

    if len(a_list) <= 1:  # prevents the code from crashing when either list is empty.
        return a_list

    pivot = a_list[-1]
    small_nums = [num for num in a_list[:-1] if num <= pivot]
    big_nums = [num for num in a_list[:-1] if num > pivot]
    return quick_sorting(small_nums) + [pivot] + quick_sorting(big_nums)


if __name__ == "__main__":
    print(quick_sorting(a))
    print(quick_sorting(b))
    print(quick_sorting(c))
    print(quick_sorting(d))
