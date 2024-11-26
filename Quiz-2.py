import random


def generate_data(size=50, seed=40, range_min=0, range_max=100):
    """Generate random integers for sorting."""
    random.seed(seed)
    return [random.randint(range_min, range_max) for _ in range(size)]


def bubble_sort(arr):
    """Sort a list using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr):
    """Sort a list using the merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def save_to_file(filename, header, data):
    """Save data to a file with a given header."""
    with open(filename, "w") as f:
        f.write(f"{header}\n")
        f.write(", ".join(map(str, data)) + "\n")


def main():
    # Generate random data
    data = generate_data()

    # Save initial data
    save_to_file("data.txt", "Data sebelum sorting:", data)

    # Perform Bubble Sort and save the result
    sorted_bubble = bubble_sort(data.copy())
    save_to_file("sorted_naive.txt", "Hasil sorting dengan Bubble Sort:", sorted_bubble)

    # Perform Merge Sort and save the result
    sorted_merge = merge_sort(data.copy())
    save_to_file("sorted_conquer.txt", "Hasil sorting dengan Merge Sort:", sorted_merge)


if __name__ == "__main__":
    main()
