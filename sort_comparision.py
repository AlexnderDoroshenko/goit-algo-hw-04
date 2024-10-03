import random
import timeit
from typing import List
from memory_profiler import memory_usage


def merge_sort(arr: List[int]) -> None:
    """
    Sorts an array in place using the merge sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr: List[int]) -> None:
    """
    Sorts an array in place using the insertion sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Function to measure time and memory usage of sorting algorithms
def measure_performance(sort_function, data):
    mem_usage = memory_usage((sort_function, (data.copy(),)), max_usage=True)
    time_taken = timeit.timeit(lambda: sort_function(data.copy()), number=100)
    return time_taken, mem_usage


if __name__ == '__main__':
    # Parameters for testing
    array_sizes = [100, 1000, 5000, 10000]
    # Testing the sorting algorithms with generated test data
    results = {}

    for size in array_sizes:
        print(f"size: '{size}'")
        random_array = [random.randint(0, 10000) for _ in range(size)]
        print(f"random_array: \n{random_array}")

        # Test Timsort (using sorted)
        results[f'Timsort size {size}'] = measure_performance(
            sorted, random_array)

        # Test Merge Sort
        results[f'Merge Sort size {size}'] = measure_performance(
            merge_sort, random_array)

        # Test Insertion Sort
        results[f'Insertion Sort size {size}'] = measure_performance(
            insertion_sort, random_array)

    # Output results
    for key, (time_taken, memory_used) in results.items():
        print(f"{key}: Time = {time_taken:.5f} seconds, Memory = {
            memory_used:.5f} MiB")


"""
Timsort size 100: Time = 0.00039 seconds, Memory = 23.94141 MiB
Merge Sort size 100: Time = 0.01548 seconds, Memory = 23.94922 MiB
Insertion Sort size 100: Time = 0.02269 seconds, Memory = 23.95703 MiB
Timsort size 1000: Time = 0.00983 seconds, Memory = 24.06250 MiB
Merge Sort size 1000: Time = 0.23282 seconds, Memory = 24.07031 MiB
Insertion Sort size 1000: Time = 2.58922 seconds, Memory = 24.07031 MiB
Timsort size 5000: Time = 0.06555 seconds, Memory = 24.44922 MiB
Merge Sort size 5000: Time = 1.36946 seconds, Memory = 24.44922 MiB
Insertion Sort size 5000: Time = 68.86770 seconds, Memory = 24.44922 MiB
Timsort size 10000: Time = 0.14268 seconds, Memory = 24.48828 MiB
Merge Sort size 10000: Time = 2.93332 seconds, Memory = 24.49219 MiB
Insertion Sort size 10000: Time = 299.84429 seconds, Memory = 24.49609 MiB

The algorithms are quite well optimized in terms of RAM usage,
but the sorting speed seems to be better for native sorting,
and with increasing test data, Merge Sort shows itself well
and is much inferior to the previous Insertion Sort algorithm.
"""
