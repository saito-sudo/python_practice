import random

# 1. スイカの位置をランダムに決める
goal_x = random.randint(0, 5)
goal_y = random.randint(0, 5)

# プレイヤーのスタート位置（0,0）
current_x = 0
current_y = 0

print("スイカ割りゲーム開始！")
print("n:北(y-1), s:南(y+1), e:東(x+1), w:西(x-1)")

# 2. ゴールに着くまで繰り返す
while current_x != goal_x or current_y != goal_y:
    distance = abs(goal_x - current_x) + abs(goal_y - current_y)
    print(f"今の場所:({current_x},{current_y}) 距離:{distance}")
    
    move = input("進む方向(n/s/e/w)を入力してね: ")

    # 3. 入力チェック
    if move not in ["n", "s", "e", "w"]:
        print("【エラー】n, s, e, w のいずれかを入力してください。")
        continue

    # 4. 移動処理（座標の加減算）
    if move == "n":
        current_y = current_y - 1
    elif move == "s":
        current_y = current_y + 1
    elif move == "e":
        current_x = current_x + 1
    elif move == "w":
        current_x = current_x - 1

# 5. ループを抜けたら終了
print(f"おめでとう！座標({goal_x},{goal_y})でスイカを見つけたよ！")