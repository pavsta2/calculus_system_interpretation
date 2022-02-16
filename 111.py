def bin_search(list_, item):
    low = 0
    high = len(list_) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if item > list_[mid]:
            low = mid + 1
        elif item == list_[mid]:
            break
        else:
            high = mid - 1
    return mid


def bin_search_rec(list_, low, high, item):
    mid = (low + high) // 2
    if item == list_[mid]:
        return mid
    elif item > list_[mid]:
        return bin_search_rec(list_, mid + 1, high, item)
    else:
        return bin_search_rec(list_, low, mid - 1, item)


if __name__ == "__main__":
    a = bin_search_rec([1, 2, 4, 6, 7, 9], 0,5,2)
    print(a)
