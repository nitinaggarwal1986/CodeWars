def maxSequence(arr):
    maxSum = 0
    n = len(arr)
    if n == 0:
        return 0
    for i in range(n):
        for j in range(i, n+1):
            temp = sum(arr[i:j])
            if maxSum <= temp:
                maxSum = temp
    return maxSum