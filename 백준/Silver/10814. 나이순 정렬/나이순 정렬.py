n=int(input())
lst = []
for i in range(n):
    a,b = map(str,input().split())
    lst.append([int(a),b])
lst = sorted(lst,key = lambda x : x[0] )
for i in lst:
    print(i[0],end=' ')
    print(i[1])