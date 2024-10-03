import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merges k sorted lists into a single sorted list.

    Args:
        lists (List[List[int]]): A list of k sorted lists to be merged.

    Returns:
        List[int]: A single merged and sorted list.
    """
    min_heap = []

    # Add the first element from each list to the heap
    for i in range(len(lists)):
        if lists[i]:  # If the list is not empty
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    merged_list = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # If there are more elements in the list
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(
                min_heap, (next_value, list_index, element_index + 1))

    return merged_list


# Testing merge_k_lists function
def test_merge_k_lists():
    test_cases = [
        # Test case 1: Basic case with multiple sorted lists
        {
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6]
        },
        # Test case 2: Case with empty lists
        {
            "input": [[], [1, 2], []],
            "expected": [1, 2]
        },
        # Test case 3: All lists are empty
        {
            "input": [[], [], []],
            "expected": []
        },
        # Test case 4: Single list
        {
            "input": [[5, 10, 15]],
            "expected": [5, 10, 15]
        },
        # Test case 5: Multiple empty and non-empty lists
        {
            "input": [[], [3, 4], [], [1, 2]],
            "expected": [1, 2, 3, 4]
        },
    ]

    for i, case in enumerate(test_cases):
        result = merge_k_lists(case["input"])
        assert result == case["expected"], f"Test case {
            i + 1} failed: expected {case['expected']}, got {result}"

    print("All test cases passed!")


# Run tests
test_merge_k_lists()
