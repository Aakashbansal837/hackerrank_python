arr = [[input(), float(input())] for i in range (int(input()))]
s = sorted(set([x[1] for x in arr]))
sort = sorted(x[0] for x in arr if x[1] == s[1])
for name in sort:
    print (name)
