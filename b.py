num = int(input())

point_2 = 0
point_1 = 0

flut =[]


for i in range(num):
    fluts = input().split()
    print(fluts)
    flut.append(list(fluts[0]))
    print(a)
    flut.append(list(fluts[1]))
    print(b)
    c = "".join(a)
    print(c)
    d = "".join(b)
    print(d)
    n = len(b)
    for j in range(n):
        if c == d:
            point_2 += 2 /len(a)
        elif a[j] == b[j] and len(c) == len(b):
            point_1 += 1/len(a)

print(flut)   
print(int(point_1) + int(point_2))