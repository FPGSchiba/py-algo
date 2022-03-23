"""
Algorithms are from here: https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_sorts
"""
import math
from heapq import heappop, heappush


def quicksort(array: list) -> list:
    """
    Quicksort Algorithm, implemented with the Explanation on: https://en.wikipedia.org/wiki/Quicksort
    :param array: The array, that should be sorted using the QuickSort Algorithm
    :return: The sorted array
    """
    elements = len(array)

    if elements < 2:
        return array

    current_position = 0

    for i in range(1, elements):
        if array[i] <= array[0]:
            current_position += 1
            temp = array[i]
            array[i] = array[current_position]
            array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position]
    array[current_position] = temp

    left = quicksort(array[0:current_position])
    right = quicksort(array[current_position + 1:elements])

    array = left + [array[current_position]] + right

    return array


def merge_sort(array: list) -> list:
    """
    Merge Sort Algorithm, implemented with the Explanation on: https://en.wikipedia.org/wiki/Merge_sort
    :param array: The array, that should be sorted using the Merge sort Algorithm
    :return: The sorted array
    """
    list_length = len(array)
    if list_length == 1:
        return array
    mid_point = list_length // 2
    left_partition = merge_sort(array[:mid_point])
    right_partition = merge_sort(array[mid_point:])
    return merge(left_partition, right_partition)


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def introsort(array: list) -> list:
    """
    Introsort Algorithm, implemented with the Explanation on: https://en.wikipedia.org/wiki/Introsort
    :param array: The array, that should be sorted using the Introsort Algorithm
    :return: The sorted array
    """
    depth_limit = 2 * math.floor(math.log2(len(array)))
    return introsort_util(array, 0, len(array) - 1, depth_limit)


def introsort_util(array: list, begin: int, end: int, depthLimit: int) -> list:
    if depthLimit == 0:
        array = heapsort(array)
        return array

    pivot = len(array) // 2
    (array[pivot], array[end]) = (array[end], array[pivot])

    partition_point, array = introsort_partition(array, begin, end)

    array = introsort_util(array, begin, partition_point - 1, depthLimit - 1)
    array = introsort_util(array, partition_point + 1, end, depthLimit - 1)
    return array


def introsort_partition(array: list, low: int, high: int):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1, array


def heapsort(array: list) -> list:
    """
    Heapsort Algorithm, implemented with the Explanation on: https://en.wikipedia.org/wiki/Heapsort
    :param array: The array, that should be sorted using the Heapsort Algorithm
    :return: The sorted array
    """
    h = []
    for value in array:
        heappush(h, value)
    array = []
    array = array + [heappop(h) for _ in range(len(h))]
    return array


def insertion_sort(array: list) -> list:
    """
    Insertion sort Algorithm, implemented with the Explanation on: https://en.wikipedia.org/wiki/Insertion_sort
    :param array: The array, that should be sorted using the Insertion sort Algorithm
    :return: The sorted array
    """
    return insertion_sort_helper(array, len(array) - 1)


def insertion_sort_helper(array: list, num: int) -> list:
    if num > 0:
        insertion_sort_helper(array, num - 1)
        x = array[num]
        j = num - 1
        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x
    return array


def block_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Block_sort
    :return: None
    """
    return None


def timsort():
    """
    Do from here: https://en.wikipedia.org/wiki/Timsort
    :return: None
    """
    return None


def selection_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Selection_sort
    :return: None
    """
    return None


def cubesort():
    """
    Do from here: https://en.wikipedia.org/wiki/Cubesort
    :return: None
    """
    return None


def shellsort():
    """
    Do from here: https://en.wikipedia.org/wiki/Shellsort
    :return: None
    """
    return None


def bubble_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Bubble_sort
    :return: None
    """
    return None


def exchange_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Sorting_algorithm#Exchange_sort
    :return: None
    """
    return None


def tree_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Tree_sort
    :return: None
    """
    return None


def cycle_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Cycle_sort
    :return: None
    """
    return None


def library_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Library_sort
    :return: None
    """
    return None


def patience_sorting():
    """
    Do from here: https://en.wikipedia.org/wiki/Patience_sorting
    :return: None
    """
    return None


def smoothsort():
    """
    Do from here: https://en.wikipedia.org/wiki/Smoothsort
    :return: None
    """
    return None


def strand_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Strand_sort
    :return: None
    """
    return None


def tournament_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Tournament_sort
    :return: None
    """
    return None


def cocktail_shaker_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
    :return: None
    """
    return None


def comb_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Comb_sort
    :return: None
    """
    return None


def gnome_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Gnome_sort
    :return: None
    """
    return None


def odd_even_sort():
    """
    Do from here: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
    :return: None
    """
    return None
