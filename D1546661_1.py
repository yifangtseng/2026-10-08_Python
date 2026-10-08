num = int(input("請輸入十進制數字,限定0~15之間的整數: "))
if 0 <= num <= 15:
    two_a = num % 2
    two_b = num // 2 % 2
    two_c = num // 4 % 2
    two_d = num // 8 % 2
    print(f"二進制={two_d}{two_c}{two_b}{two_a}")

    eight_a = num % 8
    eight_b = num // 8 % 8
    print(f"八進制={eight_b}{eight_a}")

    sixteen_a = num % 16
    if sixteen_a == 10:
        sixteen_a = "A"
    elif sixteen_a == 11:
        sixteen_a = "B"
    elif sixteen_a == 12:
        sixteen_a = "C"
    elif sixteen_a == 13:
        sixteen_a = "D"
    elif sixteen_a == 14:
        sixteen_a = "E"
    elif sixteen_a == 15:
        sixteen_a = "F"
    else:
        sixteen_a = sixteen_a
    print(f"十六進制={sixteen_a}")
else:
    print("輸入錯誤，請輸入0~15之間的整數")
