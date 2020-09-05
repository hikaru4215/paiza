# 2行の順番を１行にした
num_1 = list(input().split(" "))
num_2 = list(input().split(" "))
num_1[len(num_1):len(num_1)] = num_2

time = input().split()

time_1 = time[0]
time_2 = time[1]
time_3 = time[2]
time_4 = time[3]

n_1 = {num_1[0]:time_1}
n_2 = {num_1[1]:time_2}
n_3 = {num_1[2]:time_3}
n_4 = {num_1[3]:time_4}

kingin = input().split()

kin = kingin[0]
gin = kingin[1]

if n_1 > n_2:
    
elif n_1 < n_2:
    
if n_3 > n_4:
    
elif n_3 < n_4:
    
    
    
print(n_1)
print(n_2)
print(n_3)
print(n_4)


