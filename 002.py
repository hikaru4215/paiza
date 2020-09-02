# ある正の整数aとbがスペース区切りで入力されます。
# aとbを比較し大きい方の値を出力して下さい。
# aとbが同じ場合は「eq」と出力して下さい。
# 例1:10, 20       例2:3,3

input_line = input()
li = input_line.split()
int_list = list(map(int,li))
if int_list[0] == int_list[1]:
    print("eq")
else:
    print(max(int_list))