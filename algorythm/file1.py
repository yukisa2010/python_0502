# カウント
# 2から現在までの数字で割る
# 割り切れたらループ脱出
# 次のカウントへ

def get_prime_numbers(max_val):
    arr = []
    for i in range(2, max_val + 1):
        flag = False
        for j in arr:

            if i % j == 0:
                flag = True
                break
        
        if flag == False:
            arr.append(i)
    arr.insert(0,1)
    print(arr)

get_prime_numbers(10)