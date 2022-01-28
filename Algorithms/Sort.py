def bubble_sort(items: list):
    """
    The most common sorting algorithm. Worst-case performance O(n^2)
    :param items: list of values, could be anything. The algorithm will work anyway.
    :return: list of sorted items
    """
    for i in range(len(items)):
        for j in range(1, len(items) - i):
            if items[j] < items[j-1]:
                items[j-1], items[j] = items[j], items[j-1]
    return items


def quick_sort(items: list, start: int, finish: int):
    if start >= finish:
        return

    def divide(items_1: list, start_1: int, finish_1: int):
        pivot = start_1
        for i in range(start_1, finish_1):
            if items_1[i] <= items_1[finish_1]:
                items_1[pivot], items_1[i] = items_1[i], items_1[pivot]
                pivot += 1
        items_1[pivot], items_1[finish_1] = items_1[finish_1], items_1[pivot]
        return pivot
    pivot = divide(items, start, finish)
    quick_sort(items, start, pivot-1)
    quick_sort(items, pivot+1, finish)

    """
    
    :param items: 
    :return: 
    """


def insort(items: list):
    """
    Insertion sort. Worst-case performance O(n^2)
    :param items: list of values, could be anything. The algorithm will work anyway.
    :return: sorted list of items
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items


if __name__ == "__main__":
    elements = [15, 9, 1, 5, 7, 13, 6, 8]
    # elements = ["Kuba", "Ania", "Kacper", "Oskar"]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)