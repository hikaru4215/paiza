num_list = input().split()
num = list(map(int, num_list))
o_list = input().split()
o = list(map(float, o_list))

z = []
for i in range(num[1]):
    x = input().split()
    n = 0
    for j in range(num[0]):
        y = float(o[j]) * int(x[j])
        n += round(y)
    z.append(n)    
z_list = sorted(z, reverse = True)
z_list[num[2]:] = []
for i in z_list:
    print(i)