def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def search_range(arr, target):
    def find_boundary(find_left):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                if find_left:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    return [find_boundary(True), find_boundary(False)]

def find_insert_position(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 7))
print(binary_search(arr, 11))

scores = [55, 60, 60, 60, 75, 80, 90, 95]
print(search_first(scores, 60))
print(search_range(scores, 60))

credit_scores = [580, 620, 650, 680, 700, 720, 750, 780, 800]
applicant_score = 695
pos = find_insert_position(credit_scores, applicant_score)
print(f"Applicant score {applicant_score} ranks at position {pos} out of {len(credit_scores)}")
print(f"Approved: {applicant_score >= 650}")
