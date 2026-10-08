A = int(input("請輸入A按鈕狀態1(按下)或0(未按下): "))
B = int(input("請輸入B按鈕狀態1(按下)或0(未按下): "))
S = int(input("請輸入安全開關狀態1(開)或0(關): "))

if A != 0 and A != 1:
    print("輸入錯誤，請輸入1或0")
elif B != 0 and B != 1:
    print("輸入錯誤，請輸入1或0")
elif S != 0 and S != 1:
    print("輸入錯誤，請輸入1或0")
else:
    if A == B:
        middle = 0
    else:
        middle = 1
        
    if middle == 1 and S == 1:
        start = 1
    else:
        start = 0

print(f"第一個閘輸出={middle}")
print(f"允許啟動={start}")