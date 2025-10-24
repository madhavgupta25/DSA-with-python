def find_subarrays(arr, target, start=0, result=None):
    if result is None:
        result = []

    # Base case: if start index reaches end, stop
    if start == len(arr):
        return result

    # Helper function to explore subarrays starting from index 'start'
    def explore_subarrays(end, current_sum, sub):
        # Base case for end pointer
        if end == len(arr):
            return
        sub.append(arr[end])
        current_sum += arr[end]

        # Check if sum matches target
        if current_sum == target:
            result.append(sub.copy())

        # Recur for next element
        explore_subarrays(end + 1, current_sum, sub)

        # Backtrack
        sub.pop()

    # Explore all subarrays starting from 'start'
    explore_subarrays(start, 0, [])

    # Recur for next start index
    return find_subarrays(arr, target, start + 1, result)


n = int(input())
arr = [int(input()) for _ in range(n)]
target = int(input())

result = find_subarrays(arr, target)

# Print results (as you wanted — no brackets, two spaces)
for sub in result:
    print(" ".join(map(str, sub)), end="  ")
print()
print(len(result))
