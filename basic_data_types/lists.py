if __name__ == '__main__':
    N = int(input())
arr=[]
for i in range(N):
    a=input().split()
    for i in range(1,len(a)):
        a[i]=int(a[i])
    if a[0] == "insert":
        arr.insert(a[1],a[2])
    elif a[0] == "print":
        print(arr)
    elif a[0] == "remove":
        arr.remove(a[1])
    elif a[0] == "append":
        arr.append(a[1])
    elif a[0] == "sort":
        arr.sort()
    elif a[0] == "pop":
        arr.pop()
    elif a[0] == "reverse":
        arr.reverse()
        
