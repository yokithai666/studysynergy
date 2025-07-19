def find_sum_between_min_max_negatives(arr):
    if not arr or len(arr) < 3:
        return 0

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    negatives = [x for x in arr[start:end] if x < 0]
    return sum(negatives)

# Пример использования
if __name__ == "__main__":
    A = [3, -4, 5, -2, 7, 8, -1, 6]
    result = find_sum_between_min_max_negatives(A)
    print("Сумма отрицательных между min и max:", result)