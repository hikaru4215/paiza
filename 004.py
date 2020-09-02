# 2
# Paiza
# Gino
# 出力例1
# Hello Paiza,Gino.
# 入力例2
# 5
# Alice
# Bob
# Carol
# Dave
# Ellen
# 出力例2
# Hello Alice,Bob,Carol,Dave,Ellen.


n_list = []
# 数字を取得してnに代入する
input_line = input()
n = int(input_line)
# nの数字の分だけ文字列を出力してリストに追加する
for i in range(n):
    il = input()
    n_list.append(il)
print("Hello " + ",".join(n_list), end = ".")


cnt_list = []
cnt = int(input())
while cnt > 0:
    s_i = input()
    cnt_list.append(s_i)
    cnt -= 1
print("Hello " + ",".join(cnt_list), end = ".")
