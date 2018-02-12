n = int (input())
arr =input().split()
for i in range (len(arr)):
    arr[i] = int (arr[i])
arr.sort()
arr.reverse()
for i in range (len(arr)):
    if arr[0] != arr[i]:
        break
print(arr[i])
