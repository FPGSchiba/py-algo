"""
Helps for all Algos
"""


def swap(array: list, index_a, index_b) -> list:
    a = array[index_a]
    b = array[index_b]
    array[index_a] = b
    array[index_b] = a
    return array
