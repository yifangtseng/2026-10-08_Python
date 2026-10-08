A = int(input("請輸入0或1: "))
B = int(input("請輸入0或1: "))
if A != 0 and A != 1:
    print("輸入錯誤，請輸入0或1")
elif B != 0 and B != 1:
    print("輸入錯誤，請輸入0或1")
else:
    if A == 1 or B == 1:
        OR = 1
    else:
        OR = 0
    if A == 1 and B == 1:
        AND = 1
    else:
        AND = 0
    if A == B:
        XOR = 0
    else:
        XOR = 1
print(f"OR={OR}")
print(f"AND={AND}")
print(f"XOR={XOR}")