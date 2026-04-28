import random
import math

BOARD_SIZE = 5  # ボードの初期サイズ

def calc_distance(pos1, pos2):
    # ２点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    
    return math.sqrt(diff_x**2 + diff_y**2)


suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))  # スイカの位置
player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) # プレイヤーの位置

# スイカとプレイヤーの位置が異なる間、処理を繰り返す
while (suika_pos != player_pos):

    # スイカとプレイヤーの距離を表示する
    distance = calc_distance(suika_pos, player_pos)
    print("スイカへの距離:", distance)
    
    # キー入力に応じて、プレイヤーを移動する
    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    current_x, current_y = player_pos

    if c == "n":
        current_y = current_y - 1
    elif c == "s":
        current_y = current_y + 1
    elif c == "w":
        current_x = current_x - 1
    elif c == "e":
        current_x = current_x + 1

    player_pos = (current_x, current_y)

print("スイカを割りました！")