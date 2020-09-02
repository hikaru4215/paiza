num_list = []
input_line = input()
il = input_line.split()
int_il = list(map(int, il))
for i in range(10):
    num_list.append(int_il[0])
    int_il[0] = int_il[0] + int_il[1]
	
print(*num_list)

# 上下同じ答え

m_list = []
input_line = input()
il = input_line.split()
m = int(il[0])
n = int(il[1])
for i in range(10):
    m_list.append(m)
    m = m + n
    
print(*m_list)