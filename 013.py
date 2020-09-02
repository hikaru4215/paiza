# 整数 m と n が与えられます。

# m を n で割り算した商と余りを出力して下さい。


input_line = input()
il = input_line.split()
int_il = list(map(int, il))
print(int_il[0] // int_il[1], int_il[0] % int_il[1])

input_line = input()
il = input_line.split()
x = int(il[0]) // int(il[1])
y = int(il[0]) % int(il[1])
print(x, y)