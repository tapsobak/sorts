a = [5, 3, 8, 6, 2]
b = [7, 2, 8, 1]
c = [3, 1, 2]
d = [3]
e = []


def merge_sorting(a_list):

    n = len(a_list)
    if n <= 1:
        return a_list

    # Consider the pivot as the element at the middle of the list
    pivot = (n + 1) // 2

    left = merge_sorting(a_list[:pivot])
    right = merge_sorting(a_list[pivot:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Comparing elements from both lists and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # This is the where the magic is happening by adding the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    print(merge_sorting(a))
    print(merge_sorting(b))
    print(merge_sorting(c))
    print(merge_sorting(d))
    print(merge_sorting(e))
