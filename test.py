import random

def test_sorting_algorithm(sorting_function):
    test_cases = [
        ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([42], [42]),
        ([3, -1, 0, -3, 8, 5], [-3, -1, 0, 3, 5, 8]),
        ([random.randint(0, 100) for _ in range(100)], None)
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        if expected is None:
            expected = sorted(input_data)

        result = sorting_function(input_data[:])
        assert result == expected, f"Test {i + 1} nie powiódł się! \nOczekiwano: {expected}, \nOtrzymano: {result}"

    print(f"Funkcja {sorting_function.__name__} przeszła wszystkie testy.")

if __name__ == "__main__":
    from Insertion_sorting import insertion_sort
    from selection_sorting import selection_sort
    from bubble_sort import bubble_sort
    from merge_sort import merge_sort

    test_sorting_algorithm(insertion_sort)
    test_sorting_algorithm(selection_sort)
    test_sorting_algorithm(bubble_sort)
    test_sorting_algorithm(merge_sort)