# ある正の整数nが入力されます。
# 正の整数1から9に整数nをそれぞれを掛けた数を半角スペース区切りで出力して下さい。

# 例えばn=2の場合
# 2 4 6 8 10 12 14 16 18

# 入力例1
# 4
# 出力例1
# 4 8 12 16 20 24 28 32 36
# 入力例2
# 99
# 出力例2
# 99 198 297 396 495 594 693 792 891

input_line = input()
il = []
for i in range(1,10):
    n = int(input_line) * i
    il.append(n)
print(*il)
