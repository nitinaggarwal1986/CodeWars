def next_bigger(n):
  arr = [int(x) for x in str(n)]
  k = len(arr)
  for i in range(1, k):
    if arr[k-1-i] < arr[k-i]:
      x = arr[k-1-i]
      ind = arr[k-i:k].index(min([b for b in arr[k-i:k] if b > x])) + k - i
      arr[k-i-1] = arr[k-i-1] + arr[ind]
      arr[ind] = arr[k-i-1] - arr[ind]
      arr[k-i-1] = arr[k-i-1] - arr[ind]
      
      temp = arr[k-i:k]
      temp.sort()
      arr[k-i:k] = temp
      return int("".join([str(x) for x in arr]))
  
  return -1