import time


def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def print_iterations(arr):
    print("Iterations:")
    for i in range(min(5, len(arr))):
        print(arr[i], end=" ")
    print("...", end=" ")
    for i in range(max(0, len(arr) - 5), len(arr)):
        print(arr[i], end=" ")
    print()


def print_before_after(before, after):
    print("Before sorting:", before)
    print("After sorting:", after)


# Main program
numbers = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40,
           9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88,
           1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

print("Pilihan pengurutan:")
print("1. Bubble Sort")
print("2. Insertion Sort")

choice = int(input("Masukkan pilihan (1/2): "))

if choice == 1:
    sorted_numbers, time_taken = bubble_sort(numbers.copy())
    algorithm = "Bubble Sort"
elif choice == 2:
    sorted_numbers, time_taken = insertion_sort(numbers.copy())
    algorithm = "Insertion Sort"
else:
    print("Pilihan tidak valid")
    exit()

print("Hasil", algorithm)
print_iterations(sorted_numbers)
print("Waktu komputasi:", time_taken, "detik")
print_before_after(numbers, sorted_numbers)